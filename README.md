
---

# Kafka Producer-Consumer Example

This project demonstrates a simple setup using Apache Kafka for real-time data streaming with a producer and a consumer. The producer generates fake user data and sends it to a Kafka topic, while the consumer reads from the topic and processes the data. Additionally, Kafka Manager is used for monitoring and managing Kafka clusters.

## Project Structure

- **`producer.py`**: A script that sends fake user data to a Kafka topic.
- **`consumer.py`**: A script that consumes data from the Kafka topic.
- **`user_generator.py`**: A utility script that generates fake user data using the Faker library.
- **`.env`**: A file containing environment variables, such as the Kafka server address.

## Setup and Installation

### Prerequisites

- Docker (for running Kafka, Zookeeper, and Kafka Manager)
- Python 3.6+
- Kafka and Zookeeper (can be run locally using Docker)
- Python packages: `kafka-python`, `python-dotenv`, `Faker`

### Installing Dependencies

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/kafka-demo-python.git
   cd kafka-demo-python
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required Python packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up `.env` file:**
   Create a `.env` file in the root of your project with the following content:
   ```
   KAFKA_SERVER_ADDRESS=your_private_ip:9092
   ```
   Replace `your_private_ip:9092` with your actual private IP address and port.

### Running Kafka and Zookeeper with Docker

To set up Kafka and Zookeeper locally, use Docker:

1. **Start Zookeeper:**
   ```sh
   docker run -d -p 2181:2181 --name zookeeper zookeeper
   ```

2. **Start Kafka:**
   ```sh
   docker run -d -p 9092:9092 \
   -e KAFKA_ZOOKEEPER_CONNECT=your_private_ip:2181 \
   -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://your_private_ip:9092 \
   -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
   --name kafka \
   confluentinc/cp-kafka
   ```

### Running Kafka Manager with Docker

Kafka Manager provides a web interface for managing and monitoring Kafka clusters.

1. **Start Kafka Manager:**
   ```sh
   docker run -d -p 9000:9000 \
   -e ZK_HOSTS="your_private_ip:2181" \
   --name kafka-manager \
   sheepkiller/kafka-manager
   ```

2. **Access Kafka Manager**:
   - Open a web browser and go to `http://your_private_ip:9000`.
   - Add your Kafka cluster using the Zookeeper host (`your_private_ip:2181`).

Replace `your_private_ip` with your actual private IP address.

### Running the Scripts

1. **Producer**: Start the producer to generate and send fake user data.
   ```sh
   python producer.py
   ```

2. **Consumer**: Start the consumer to read and process data from the Kafka topic.
   ```sh
   python consumer.py
   ```

## Key Concepts

- **Partitions**: Kafka topics are divided into partitions, allowing for parallel data processing. Each partition is an ordered, immutable sequence of records and can be consumed by only one consumer in a consumer group at a time.

- **Consumer Groups**: A consumer group is a set of consumers that work together to consume messages from a Kafka topic. Each partition of the topic is consumed by only one consumer in the group, enabling load balancing and fault tolerance.

- **Kafka Manager**: A tool that provides a web interface for monitoring Kafka clusters. It helps manage topics, brokers, and consumers, and provides insights into cluster performance and health.

## Additional Information

- **Faker Library**: Used in `user_generator.py` to generate random user data.
- **Environment Variables**: Managed using `python-dotenv`. The `.env` file contains sensitive information like the Kafka server address.

## Troubleshooting

- **Connection Issues**: Ensure Kafka and Zookeeper are running and accessible from your machine.
- **Consumer Offset**: If messages are not appearing, check the `auto_offset_reset` parameter in the consumer configuration.
- **Environment Variables**: Ensure the `.env` file is properly set up and loaded in both `producer.py` and `consumer.py`.

---

Make sure to replace `your_private_ip` with the actual private IP address of the machine running Kafka, Zookeeper, and Kafka Manager.