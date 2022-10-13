import argparse
import json
import logging
import os
import sys
import pyflink
from pyflink.common import Duration, Row
from pyflink.common import SimpleStringSchema, Encoder
from pyflink.common.typeinfo import Types
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream import StreamExecutionEnvironment, RuntimeExecutionMode
from pyflink.datastream.connectors import FlinkKafkaProducer, FileSink, OutputFileConfig, RollingPolicy, FileSource, \
    StreamFormat, FlinkKafkaConsumer

from logic.normalizer import Normalizer


def arable_translate(input_path, output_path, isKafka):
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    kafka_jar = f"file:///{os.path.dirname(os.path.realpath(__file__))}/connectors/flink-sql-connector-kafka-1.15.2.jar"
    env.add_jars(kafka_jar)

    ds = define_source(env, input_path, isKafka)

    ds = ds \
        .flat_map(translate) \
        .map(lambda a: data_serialize(a), Types.STRING())

    emit_results(ds, output_path)

    env.execute()


def split(raw_data_string):
    print('raw_data_string', raw_data_string)
    for raw_object in json.loads(raw_data_string):
        yield raw_object


def translate(raw_data_string):
    try:
        print('raw_data_string', raw_data_string)
        for raw_object in json.loads(raw_data_string):
            obs_collection, obs_collection_id, observations = Normalizer().normalize('hourly', 'acc1', 'asset1', raw_object)
            print('normalized')
            yield observations, obs_collection

    except Exception as ex:
        print('raw_data_string', raw_data_string)
        print(ex)


def data_serialize(data):
    return json.dumps(data)


def emit_results(ds, output_path):
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

    return ds


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', required=False, help='Input file to process.')
    parser.add_argument('--output', dest='output', required=False, help='Output file to write results to.')
    parser.add_argument('--isKafka', dest='isKafka', required=False, help='isKafka')
    known_args, _ = parser.parse_known_args(sys.argv[1:])

    arable_translate(known_args.input, known_args.output, known_args.isKafka)
