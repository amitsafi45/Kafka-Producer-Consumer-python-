# producer.py
from kafka import KafkaProducer
import os
from dotenv import load_dotenv
from user_generator import registered_user
import json
import time

# Load environment variables from .env file
load_dotenv()

# JSON serialization function
def json_serialization(data):
    return json.dumps(data).encode('utf-8')

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[os.getenv('KAFKA_SERVER_ADDRESS')],
    value_serializer=json_serialization
)

if __name__ == '__main__':
    print(producer)
    while True:
        user = registered_user()  # Generate fake user data
        print(user)
        producer.send('registered_user', user)  # Send data to Kafka topic
        time.sleep(5)  # Sleep for 5 seconds before sending the next message
