from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: v.encode('utf-8')
)

for i in range(5):
    message = f"Message {i+1}"
    producer.send('demo_topic', message)
    print(f"Sent: {message}")

producer.flush()
producer.close()
