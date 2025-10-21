from kafka import KafkaProducer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='10.1.20.213:9092')

# Send messages to the 'hello_world' topic
message = 'œ∑´®†¥¨ˆøπåß∂ƒ©˙∆˚¬Ω≈ç√∫˜µ≤¬øß´®'.encode('utf-8')  # Encode the message as bytes
producer.send('class-chat', value=message)
print(f'Sent: {message}')

# Close the producer
producer.close()
