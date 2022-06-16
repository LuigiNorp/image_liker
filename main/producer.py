import pika, json

params = pika.URLParameters('amqps://mntkdxwi:V6Ce6ny8f2k3eE5SsUvyQTyIo7SWggI8@albatross.rmq.cloudamqp.com/mntkdxwi')
connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)