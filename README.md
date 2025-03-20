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

For demo, run the following

```bash
uv sync
```

This will create the .venv, then activate it using

```bash
source .venv/bin/activate
```

Then you can start the workers using the following command in separate terminal

```bash
uv run app.py
```

This will start the worker that will listen to events on queue and will compute drift report and store it in  mongo db based on the signals received.

To simulate an inference event in a separate terminal run

```bash
uv run event_generator.py
```