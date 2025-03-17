from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages
producer.send('demo_topic', b'Hello, Kafka!')
producer.send('demo_topic', b'This is a test message')
producer.flush() 

print("Messages sent successfully!")
