from celery import Celery

# Initialize Celery
celery = Celery(
    __name__,
    backend='rpc://',  # Using RPC as a simple backend for Celery
    broker='pyamqp://guest@localhost//'  # RabbitMQ broker URL
)

def make_celery(app):
    celery.conf.update(app.config)
    return celery