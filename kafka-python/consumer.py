from kafka import KafkaConsumer

consumer = KafkaConsumer('demo_topic', bootstrap_servers='localhost:9092')

print("Listening for messages...")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
