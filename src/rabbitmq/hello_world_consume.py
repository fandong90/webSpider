'''
Created on 2016年12月9日

@author: fandong
'''
#导入链接rabbitmq 的包
import pika
import sys
from multiprocessing.connection import deliver_challenge
#使用内部的函数进行链接
credentials=pika.PlainCredentials("guest","guest")
conn_params=pika.ConnectionParameters("localhost",credentials=credentials)
conn_broker=pika.BlockingConnection(conn_params)
#获取信道
channel=conn_broker.channel()
#声明交换器
channel.exchange_declare(exchange="hello-exchange",exchange_type="direct", passive=False, durable=True, auto_delete=False)
#声明队列
channel.queue_declare(queue="hello-queue")
#通过建'hola'将队列和交换器绑定
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")

def msg_consumer(channel,method,header,body):
    #相应服务器任务
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body =="quit":
        #取消消费
        channel.basic_cancel(consumer_tag="hello_consumer")
        channel.stop_consuming()
    else:
        print(body)
#获取消费信息
channel.basic_consume(msg_consumer,queue="hello-queue",consumer_tag="hello-consumer")
#停止消费信息
channel.start_consuming()





