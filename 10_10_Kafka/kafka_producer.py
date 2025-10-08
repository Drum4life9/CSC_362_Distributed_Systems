from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages to the 'hello_world' topic
for i in range(10):
    message = f'Hello World {i}'.encode('utf-8')  # Encode the message as bytes
    producer.send('quickstart-events', message)
    print(f'Sent: {message}')

# Close the producer
producer.close()
