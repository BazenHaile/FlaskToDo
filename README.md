 FlaskToDoApplication

This is a simple to-do list web application built using Flask for Python.

 Features

- Add tasks
- Delete tasks
- Edit tasks
- Mark tasks complete


FlaskToDo Application Deployment Report

Overview:This text provides the deployment details and access instructions for the 
FlaskToDo application hosted on Render.com. The FlaskToDo application is a simple 
to-do list web application built with Flask.


Deployment Details

Pre-Deployment Checklist:
•  Code is managed in a Git repository on GitHub.
•  The requirements.txt file is present and includes all necessary Python packages.
•  A .gitignore file is created to exclude non-essential files from the repository.
•  The local repository is synchronized with the GitHub repository.


Render Configuration:

•	Service Name: FlaskToDo
•	Region: Europe
•	Branch: main
•	Runtime: Python3
•	Build Command: pip install -r requirements.txt (Render automatically 
executes this command if requirements.txt is present in the repository root)
•	Start Command: gunicorn -w 4 -b :$PORT app:app
•	Environment Variables: since optional, it was not used in this project.


Deployment Steps:
1.	Created a new web service on Render.com.
2.	Connected the GitHub account and selected the FlaskToDo repository.
3.	Configured the service with the specific settings for the Flask application.
4.	Deployed the application by clicking "Create Web Service".
5.	Monitored the deployment process and reviewed logs for any potential errors.
6.	Verified the successful deployment with the 
URL to Access Application: https://flasktodoapp-p94g.onrender.com




