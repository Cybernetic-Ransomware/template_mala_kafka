# Template Project: Docker + Kafka

Quick implementation of a containerized Kafka instance 

---
## Requirements
- Docker Desktop,
- Docker Compose,
- Python >= 3.12.

## Initialization

1. Clone the repository:
    ```bash
    git clone https://github.com/Cybernetic-Ransomware/template_mala_kafka.git
    ```
2. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
4. Install dependencies:
    ```bash
    pip install kafka-python==2.0.2 six==1.16.0
    ```
5. Run Docker Desktop and start the Kafka container:
    ```bash
    docker-compose up --build
    ```
6. Run the consumer and producer to test message sending:
    ```bash
    python ./main/cons.py
    python ./main/prod.py
    ```

---

## Useful Links and Documentation

- Kafka Python client: [https://pypi.org/project/kafka-python/)
