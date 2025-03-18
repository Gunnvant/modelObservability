## Basic Examples using RabbitMQ Service

For these examples to run, make sure you have RabbitMQ installed and running on your machine. If you have docker up and running you can run the following commands to start a RabbitMQ container:

```bash
docker run --name rabbit3 -p 5672:5672 -p 15672:15672 -d rabbitmq:3-management
```
Then you make sure that the env variables are set up. Use the [shell](../../env.sh) script to set up the env variables.

```bash
source env.sh
```
You can then start the producer and consumer services in separate terminals.

```bash
uv run python cli_producer.py
```

```bash
uv run python cli_consumer.py
```