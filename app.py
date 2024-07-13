from flask import Flask, request
from celery import Celery
from celery.utils.log import get_task_logger
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


# Initialize Flask application
app = Flask(__name__)

# Configure Celery settings
app.config['CELERY_BROKER_URL'] = 'amqp://localhost'  # RabbitMQ broker URL
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'  # Result backend for Celery tasks

# Initialize Celery instance
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Initialize logger for Celery tasks
logger = get_task_logger(__name__)

# Celery task to send email
@celery.task(bind=True)
def send_email_task(self, to_email):
    subject = "Test Email"
    body = "This is a test of the application"

    # Email credentials (should be handled securely in production)
    sender_email = "oluwasesanrotimi2@gmail.com"
    sender_password = "cezlmrzsloeuaawu"


    # Construct email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        # Log error if email sending fails and retry after 60 seconds
        logger.error(f"Failed to send email to {to_email}: {str(e)}")
        raise self.retry(exc=e, countdown=60)

# Route for the home page
@app.route('/')
def index():
    return 'Messaging System with RabbitMQ/Celery and Python Flask'

# Route to trigger email sending task
@app.route('/sendmail', methods=['GET'])
def send_mail():
    to_email = request.args.get('sendmail')
    if to_email:
        send_email_task.delay(to_email)  # Queue the email sending task asynchronously
        return f"Email sending task queued for {to_email}"
    else:
        return "No email address provided"

# Route to log a message
@app.route('/talktome', methods=['GET'])
def talk_to_me():
    try:
        # Log the current timestamp and a message to a file
        with open('/var/log/messaging_system.log', 'a') as log_file:
            log_file.write(f"{datetime.now()} - Log entry\n")
        return "Logged successfully"
    except Exception as e:
        return f"Failed to log: {str(e)}"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
