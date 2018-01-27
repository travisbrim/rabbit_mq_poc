from kombu import Connection, Exchange, Queue

common_exchange = Exchange('common', 'direct', durable=True)
email_queue = Queue('email', exchange=common_exchange, routing_key='template')
send_queue = Queue('send', exchange=common_exchange, routing_key='send')

def template_processing(body, message):
    print '[x] recieved {}: {}'.format(body['addr'], body['context'])
    producer = conn.Producer(serializer='json')
    producer.publish({'addr': body['addr'], 'msg': '<h1>{}</h2>'.format(body['context'])},
                      exchange=common_exchange, routing_key='send',
                      declare=[send_queue])
    print '[x] published'
    message.ack()

with Connection('amqp://guest:guest@localhost//') as conn:

    with conn.Consumer(email_queue, callbacks=[template_processing]) as consumer:
        while True:
            print 'Listening...'
            conn.drain_events()
