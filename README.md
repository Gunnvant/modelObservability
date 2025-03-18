## DataDrift Service

**Purpose**: 

1. Uses evidently to run data drift analysis on two datasets. 
2. Saves drift results in mongodb collection.
3. Listens to events from a rabbitmq queue to initiate drift analysis.
4. Writes logs of drift computation to mongo db collection.
5. Writes alerts to a rabbitmq queue in case of drift detection.

**Run Unit tests**

```bash
uv run pytest rabbitmq_tests.py
uv run pytest mongodb_tests.py
```

**Run Coverage Tests**

```bash     
uv run pytest --cov=rabbitMQService/ rabbitmq_tests.py
uv run pytest --cov=mongoDBService/ mongodb_tests.py
```