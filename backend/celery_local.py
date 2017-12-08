from .celery import *

# To use celery in memory
#task_always_eager = True

broker_url = 'amqp://taiga:taiga@rabbitmq:5672/'
result_backend = 'rpc://'