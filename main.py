import argparse
import json
import logging
import os
import sys

from pyflink.common import Duration, Row
from pyflink.common import SimpleStringSchema, Encoder
from pyflink.common.typeinfo import Types
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaProducer, FileSink, OutputFileConfig, RollingPolicy, FileSource, \
    StreamFormat, FlinkKafkaConsumer

from logic.normalizer import Normalizer


def arable_transform(input_path, output_path, isKafka):
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    kafka_jar = f"file:///{os.path.dirname(os.path.realpath(__file__))}/connectors/flink-sql-connector-kafka-1.15.2.jar"
    env.add_jars(kafka_jar)

    ds = define_source(env, input_path, isKafka)

    # map
    def transform(data):
        try:
            raw_object = json.loads(data)
            obs_collection, obs_collection_id, observations = Normalizer().normalize('hourly', 'acc1', 'asset1',
                                                                                     raw_object)
            return Row(json.dumps(observations), json.dumps(obs_collection))
        except Exception as ex:
            print('data', data)
            print(ex)

    def data_serialize(data):
        return json.dumps(data)

    ds = ds.flat_map(transform).map(lambda a: data_serialize(a), Types.STRING())

    if output_path is not None:
        ds.sink_to(
            sink=FileSink.for_row_format(
                base_path=output_path,
                encoder=Encoder.simple_string_encoder("utf-8"))
            .with_output_file_config(
                OutputFileConfig.builder()
                .with_part_prefix("prefix")
                .with_part_suffix(".ext")
                .build())
            .with_rolling_policy(RollingPolicy.default_rolling_policy())
            .build()
        )
    else:
        print("Printing result to stdout. Use --output to specify output path.")
        ds.print()
        kafka_producer = FlinkKafkaProducer(
            topic='dest_topic',
            serialization_schema=SimpleStringSchema(),
            producer_config={'bootstrap.servers': 'localhost:9092', 'group.id': 'test_group'})
        ds.add_sink(kafka_producer)

    env.execute()


def define_source(env, input_path, is_kafka):
    if input_path is not None:
        ds = env.from_source(
            source=FileSource.for_record_stream_format(StreamFormat.text_line_format(), input_path).
            process_static_file_set().build(),
            watermark_strategy=WatermarkStrategy.for_monotonous_timestamps(),
            source_name="file_source"
        )
    elif is_kafka:
        kafka_props = {'bootstrap.servers': 'localhost:9092', 'group.id': 'pyflink-e2e-source'}
        kafka_consumer = FlinkKafkaConsumer("source_topic", SimpleStringSchema(), kafka_props)

        watermark_strategy = WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(5))

        kafka_consumer.set_start_from_earliest()
        ds = env.add_source(kafka_consumer).assign_timestamps_and_watermarks(watermark_strategy)
    else:
        collection_data = [
            (1,
             '{"mint":7.2,"b4dw":0.003,"location":"609e6b21b9ffd300120a9492","etc":null,"rh":85,"max_tdew":4.8,"b6uw":0.005,"precip":0,"prate":null,"et":0,"b1uw":0.004,"b6dw":0.005,"b2uw":0.002,"b2dw":0.002,"tabove":null,"rh_at_maxt":85,"tdew":4.8,"update_time":"2022-01-13 09:25:34+00","wind_speed":null,"wind_speed_max":null,"device":"C006765","b3dw":0.003,"p":103.4,"slp":104.7,"time":"2022-01-12T14:00:00Z","wind_direction":null,"ea":0.86,"paruw":-3.5,"low_quality":false,"b5dw":0.002,"b1dw":0.005,"lwdw":null,"swuw":-1.8,"b7uw":0.001,"swdw":1.7,"maxt":7.2,"b3uw":0.004,"b5uw":0.002,"pardw":2.9,"wind_heading":null,"tbelow":8.4,"et_version":"20210128_1","min_rh":85,"wind_speed_min":null,"tair":7.2,"vpd":0.2,"b7dw":0.001,"b4uw":0.004,"lat":52.07336,"lwuw":-356.3,"lfw":0,"sample_pct":0.08,"long":8.69779}'),
            (2,
             '{"mint":6.5,"b4dw":0.003,"location":"609e6b21b9ffd300120a9492","etc":null,"rh":84,"max_tdew":4.9,"b6uw":0.004,"precip":0,"prate":null,"et":0,"b1uw":0.003,"b6dw":0.004,"b2uw":0.002,"b2dw":0.002,"tabove":null,"rh_at_maxt":83,"tdew":4.6,"update_time":"2022-01-14 09:48:00+00","wind_speed":null,"wind_speed_max":null,"device":"C006765","b3dw":0.003,"p":103.4,"slp":104.7,"time":"2022-01-12T15:00:00Z","wind_direction":null,"ea":0.85,"paruw":-2.9,"low_quality":false,"b5dw":0.002,"b1dw":0.004,"lwdw":null,"swuw":-1.5,"b7uw":0.001,"swdw":1.4,"maxt":7.5,"b3uw":0.003,"b5uw":0.002,"pardw":2.3,"wind_heading":null,"tbelow":6.6,"et_version":"20210128_1","min_rh":83,"wind_speed_min":null,"tair":7.1,"vpd":0.2,"b7dw":0.001,"b4uw":0.003,"lat":52.07336,"lwuw":-347.4,"lfw":0,"sample_pct":1,"long":8.69779}')
        ]
        ds = env.from_collection(
            collection=collection_data,
            type_info=Types.ROW_NAMED(["id", "raw"], [Types.INT(), Types.STRING()])
        )
    return ds


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', required=False, help='Input file to process.')
    parser.add_argument('--output', dest='output', required=False, help='Output file to write results to.')
    parser.add_argument('--isKafka', dest='isKafka', required=False, help='isKafka')
    known_args, _ = parser.parse_known_args(sys.argv[1:])

    arable_transform(known_args.input, known_args.output, known_args.isKafka)
