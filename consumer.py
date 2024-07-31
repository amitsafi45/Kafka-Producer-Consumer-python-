# consumer.py
from kafka import KafkaConsumer
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    # Initialize Kafka consumer
    consumer = KafkaConsumer(
        "registered_user",  # Kafka topic
        bootstrap_servers=[os.getenv('KAFKA_SERVER_ADDRESS')],  # Kafka server address
        auto_offset_reset='earliest',  # Start consuming from the earliest message
        group_id='amit_consumer_one'  # Consumer group ID
    )
    print("Starting consuming")
    
    # Consume messages from Kafka topic
    for msg in consumer:
        print('Registered User {}'.format(json.loads(msg.value)))
