from celery_app import celery
import smtplib

@celery.task
def send_mail_task(email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your-email@gmail.com", "your-password")
        message = "Subject: Testing Phase\n\nHello, this is a testing phase."
        server.sendmail("your-email@gmail.com", email, message)
        server.quit()
        return "Email sent successfully."
    except Exception as e:
        return str(e)