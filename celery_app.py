from celery import Celery

def make_celery(app):
    celery = Celery(
    __name__,
    backend='rpc://',  # Example: Using RPC as backend
    broker='pyamqp://guest@localhost//'  # Example: Using RabbitMQ as broker
)

def make_celery(app):
    celery.conf.update(app.config)
    return celery