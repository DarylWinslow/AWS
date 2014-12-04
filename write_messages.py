import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='KIAIR7EH3TNSTDUCWKA', aws_secret_access_key='t2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHZ')

rs = conn.get_all_queues()
for q in rs:
	print q.id



# write a message to the queue
m = Message()
m.set_body('Hello to you!')
q.write(m)


#write 100 messages to the queue
i=0

for i in range(0, 99):
	m.set_body('All the messages'+i)
	q.write(m)



#read a message from queue
rs = q.get_messages()
m = rs[27]
m.get_body()


#delete a message
q.delete_message(m)
