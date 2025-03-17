from kafka.admin import KafkaAdminClient, NewTopic

# Connect to Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="my_admin"
)

# Define topic
topic_name = "demo_topic"
topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)

# Create topic
admin_client.create_topics([topic])
print(f"Topic '{topic_name}' created successfully!")

# Close client
admin_client.close()
