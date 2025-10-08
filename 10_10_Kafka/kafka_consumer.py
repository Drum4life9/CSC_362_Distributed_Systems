from kafka import KafkaConsumer
consumer = KafkaConsumer('quickstart-events')
for msg in consumer:
    print (msg)