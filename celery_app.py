from celery import Celery

def make_celery(app):
    celery = Celery(
    app.import_name,
    backend='rpc://',  # Example: Using RPC as backend
    broker='pyamqp://guest@localhost//'  # Example: Using RabbitMQ as broker
    )
    celery.conf.update(app.config)
    return celery


