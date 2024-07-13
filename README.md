# Messaging System with RabbitMQ, Celery, Flask, and Nginx Setup

   This project demonstrates a messaging system using RabbitMQ for message queuing, Celery for asynchronous task processing, Flask as the web framework, and Nginx for reverse proxy and serving static files. This README provides instructions for setting up and running the application.

## Prerequisites

   Before running the application, ensure you have the following installed:

   - Python 3.x
   - RabbitMQ
   - Nginx (optional for production deployment)
   - Virtual environment tool (e.g., virtualenv)

## Installation

   - Clone the repository:
   
   </pre>

   ``` bash

      git clone https://github.com/mroluwasesan/Messaging-System.git
      cd Messaging-System 
      
   ```
   </pre>

   -  Set up virtual environment:

   </pre>

   ``` bash

   python3 -m venv myenv
   source myenv/bin/activate

   ```

   </pre>

   - Install dependencies:

   </pre>

   ``` bash

   pip install -r requirements.txt
   
   ```

   </pre>


   ## Create the Log File:

   Ensure the log file exists:

    </pre>

   ```bash

   sudo touch /var/log/messaging_system.log
     
   ```

   </pre>

   ## Change Ownership to the Current User:
   Change the ownership of the log file to the user who will run the application:

    </pre>

   ```bash

   sudo chown $USER:$USER /var/log/messaging_system.log
  
   ```

   </pre>

   - Configure RabbitMQ:
   
      Ensure RabbitMQ is installed and running. Update CELERY_BROKER_URL in `app.py` if necessary.

   ## Running the Application

   ## Starting RabbitMQ
   
   Start RabbitMQ server if not already running:

   </pre>

   ``` bash

   sudo systemctl start rabbitmq-server

   ```

   </pre>

   ## Starting Celery Worker

   In the virtual environment, start Celery worker for processing tasks:

   </pre>

   ``` bash

      celery -A tasks worker --loglevel=info
      
   ```
   </pre>

   ## Running Flask Application
   
   In a separate terminal within the virtual environment, run the Flask application:

   </pre>

   ``` bash

      python app.py

   ```
   </pre>

   ## Accessing the Application
   - Open a web browser and navigate to http://localhost:5000/.
   - Use query parameters ?sendmail=<email_address> or ?talktome=true to test email sending and logging functionalities. 
   
   ## Nginx Configuration (for production)

   Configure Nginx to serve the Flask application and handle static files. Example configuration:
   - sample file in the nginx.conf file within the config folder.
   - Replace example.com with your domain and /path/to/static/files with the actual path to your static files directory.


   ## Testing the Endpoints
   - Use ngrok to expose your local Flask application (ngrok http 5000). Then, access the endpoints:

   - Send email: http://your_ngrok_url/sendmail?sendmail=you_email@gmail.com
   - Log entry: http://your_ngrok_url/talktome

   ## Contributing

   Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

