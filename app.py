from flask import Flask, request
from celery_app import make_celery
from tasks import send_mail_task
import logging
import os

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = make_celery(app)

logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_mail_task.delay(sendmail)
        return f"Email to {sendmail} has been queued."

    if talktome:
        logging.info(f"Talk to me request received at {os.path.join(os.path.dirname(__file__), '/var/log/messaging_system.log')}")
        return "Current time has been logged."

    return "Welcome to the messaging system!"

if __name__ == '__main__':
    app.run(debug=True)
