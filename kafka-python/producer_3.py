import csv
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'demo_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

print("Listening for messages...")

with open("messages.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    if file.tell() == 0:
        writer.writerow(["Message"])
    
    for message in consumer:
        decoded_message = message.value.decode('utf-8')
        print(f"Received: {decoded_message}")
        writer.writerow([decoded_message])
        file.flush()
