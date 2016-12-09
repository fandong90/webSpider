'''
Created on 2016年12月9日

@author: fandong
'''
import pika
import sys
#链接到rabbitmq
credentials=pika.PlainCredentials("guest","guest")
conn_params=pika.ConnectionParameters("localhost",credentials=credentials)
conn_broker=pika.BlockingConnection(conn_params)
#获取信道
channel=conn_broker.channel()
#声明交换器
channel.exchange_declare(exchange="hello-exchange",exchange_type="direct", passive=False,durable=True,auto_delete=False)
#创建纯文本信息
msg=sys.argv[1]
msg_props=pika.BasicProperties()
msg_props.content_type="text/plain"
#发布信息
channel.basic_publish(body=msg, exchange="hello-exchange", properties=msg_props, routing_key="hola")


