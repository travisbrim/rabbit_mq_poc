import sys

from kombu import Connection, Exchange, Queue

common_exchange = Exchange('common', 'direct', durable=True)
email_queue = Queue('email', exchange=common_exchange, routing_key='email')

with Connection('amqp://guest:guest@localhost//') as conn:

    producer = conn.Producer(serializer='json')
    producer.publish({'addr': sys.argv[1], 'context': {'test': sys.argv[2]}},
                      exchange=common_exchange, routing_key='template',
                      declare=[email_queue])
