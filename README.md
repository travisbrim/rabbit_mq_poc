# rabbit-mq-poc

1. template queue

each message processed once.  work queue.  all consumers should be listening for same messages

2. send queue

sent from template workers, emailed out.  work queue.  routing key for priority?

3. status

sent from send workers, sent on to status consumers

status should probably be a topic exchange, so likely a 'notifications' exchange necessary in addition to 'common'
