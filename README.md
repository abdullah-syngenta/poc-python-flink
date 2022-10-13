# poc-python-flink

### prerequisites:
1. deploy a kafka docker container https://www.conduktor.io/kafka/how-to-start-kafka-using-docker#How-to-run-Kafka-with-Docker
2. create source and destination topics 

`kafka-topics --bootstrap-server localhost:9092 --topic source_topic --create --partitions 3 --replication-factor 1`

`kafka-topics --bootstrap-server localhost:9092 --topic dest_topic --create --partitions 3 --replication-factor 1`

### steps to run:
1. pipenv install --dev
2. pipenv run start-kafka
3. produce messages to the source topic.
4. check for the messages produced on the destination topic.