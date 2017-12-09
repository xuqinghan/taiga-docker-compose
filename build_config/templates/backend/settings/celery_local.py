from .celery import *

# To use celery in memory
#task_always_eager = True

broker_url = 'amqp://{{RABBITMQ_DEFAULT_USER}}:{{RABBITMQ_DEFAULT_PASS}}@{{RABBITMQ_SERVER}}:5672/'
result_backend = 'rpc://'
