import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAR7EH3TNSTDUCWKA', aws_secret_access_key='t2FZT5mrLYy8gX7kS1q0p4ObQYXTwGnaiUm+rxHZ'

myqueue = conn.create_queue('c12730541')

print myqueue

#Write a message to queue
m = Message()
m.set_body('Buongiorno mondo')
myqueue.write(m)
