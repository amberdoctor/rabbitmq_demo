#!/usr/bin/env python
import pika
import jsonpickle

class TestObject(object):
	def __init__(self, name):
		self.name = name

if __name__ == "__main__":

	connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='hello')

	print ' [*] Waiting for messages. To exit press CTRL+C'

	def callback(ch, method, properties, body):
		print " [x] Received " + jsonpickle.decode(body).name

	channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

	channel.start_consuming()
