import asyncio

from clean_architecture import (
    init_collections,
    BasedConsumerRunner,
    ConfiguredKafkaConsumer,
    InternalEventConsumerKafkaConfig)

from src.applications import ActionLogCreatingCommand

INTERNAL_EVENTS = {
    'action.log': ActionLogCreatingCommand
}

if __name__ == '__main__':
    consumer = ConfiguredKafkaConsumer(InternalEventConsumerKafkaConfig())
    runner = BasedConsumerRunner(consumer, INTERNAL_EVENTS, worker_name='Hehe')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_collections())
    loop.run_until_complete(runner.consume())
