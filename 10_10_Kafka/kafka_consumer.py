from kafka import KafkaConsumer
consumer = KafkaConsumer('sample-events', bootstrap_servers='10.1.20.213:9092')
for msg in consumer:
    print (msg)