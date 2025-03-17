from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'demo_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  
    enable_auto_commit=True       
)

print("Listening for messages...")
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
