from flask import Flask, request
from celery import Celery
import smtplib
import logging
from datetime import datetime

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@rabbitmq//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

@celery.task
def send_email(to_email):
    with smtplib.SMTP('localhost') as server:
        server.sendmail('your_email@example.com', to_email, 'This is a test email')

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return f"Email will be sent to {sendmail}"
    
    if talktome:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"Talk to me requested at {current_time}")
        return "Current time logged."

    return "Welcome to the messaging system!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
