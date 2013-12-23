#!/usr/bin/env python
import pika
import jsonpickle

class TestObject(object):
	def __init__(self, name):
		self.name = name

def send_message(message):
	channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=jsonpickle.encode(message))
	print " [x] Sent " + jsonpickle.encode(message)



if __name__ == "__main__":
	connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='hello')

	send_message(TestObject("Hello World JSON serialize!"))

	connection.close()
