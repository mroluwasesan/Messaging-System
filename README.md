# Messaging System with RabbitMQ/Celery and Python Flask

This project demonstrates a messaging system built with RabbitMQ, Celery, and Python Flask. It allows sending emails asynchronously and logging actions to a file.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- RabbitMQ
- Celery
- Flask
- Necessary Python packages (install using pip install -r requirements.txt)


## Installation

- Clone the repository:

bash

git clone https://github.com/mroluwasesan/Messaging-System.git

cd messaging-system

- Install dependencies:

bash

pip install -r requirements.txt

- Configure Gmail SMTP:

Enable less secure app access in your Gmail account settings or generate an app-specific password.
Update sender_email and sender_password in app.py with your Gmail credentials.

- Start RabbitMQ:

bash

sudo service rabbitmq-server start

- Start Celery worker:

bash

celery -A app worker --loglevel=info

- Run the Flask application:

bash

python app.py

## Usage

- Access the Flask application at http://localhost:5000.
- Endpoints:
   - /sendmail?sendmail=destination_email@example.com: Sends a test email to the specified email address.
   - /talktome: Logs the current time to /var/log/messaging_system.log.

## Nginx Configuration

Sample Nginx configuration to proxy requests to the Flask application:

nginx

server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

Replace your_domain.com with your actual domain.

