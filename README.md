Resource Center
------------------

This is a basic application that provides a portal to add and edit classes, along with assigning favorite classes to the assigned student

The application is broken up into 2 modules, courses and students. The url routes are located in environment directory under LearningApp/urls.py
The students.views API is simplistic to demonstrate a basic transaction in django
The api's in courses utilize django rest framework, which adds structured classes and mixins to streamline transactions

The ui demonstrates RESTful GET/PUT/POST/DELETE operations through AJAX requests, which are gated through a csrf token.


the admin interface is located at 127.0.0.1:8000/admin
Although I did not flesh out any admin interfaces for these data models, this is a good out-of-the-box view of the records in the applications database

============
Installation


Pull the repo down
git clone https://github.com/arnol229/learningapp && cd learningapp

Install application dependencies with pip (sudo apt-get install pip)
pip install -r REQUIREMENTS.txt

deploy:
chmod ./deploy.sh +x
./deploy.sh

============
Walkthrough

navigate to 127.0.0.1:8000

The app comes loaded with a sample user to search for: "John Doe"
Searching this (or any) name will bring all available the students enrolled classes in the payload of the response. this data has not been hooked up to a view on the webpage