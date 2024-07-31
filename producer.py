from kafka import KafkaProducer
import os
producer = KafkaProducer(configs=[os.getenv('KAFKA_SERVER_ADDRESS')])
