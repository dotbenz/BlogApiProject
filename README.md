BlogApi

This is an Api using the django and django rest_framework that has a database with over 200 rows of data.

Description
The Api contains several endpoints to get information about BlogPosts from the database. Each BlogPost has the following parameters: a title, content, author, and timestamp

Installation
I used the django package manager to install all of the dependencies for this project pip insatll django pip instal djangorestframework. The JWT package was also
installed with the command pip install djangorestframework-simplejwt. I also used pip to install faker. faker allowed me to generate dummy data for my database.
All dependencies are found in the requirements.txt file

EndPoints and Usage
Each endpoint is included in the Documentation on Insomnia. I have decided to use Insomnia for my Api Testing/Documentation.
Firstly, a user needs to be authenticated, to get authenticated, send a post request to http://localhost:8000/api/token/
with your username and password. You can then have access to get all BlogPosts using the endpoint http://localhost:8000/api/posts/,
get a particular BlogPost with the endpoint http://localhost:8000/api/posts/id/. You can also update and delete
BlogPosts as demonstrated in the Video presentation. 
I implemented JWT for authentication and authorization. The access token is set to 60 minutes while
the refresh token has been set to one day. Once the access token expires, you can send a post request to
http://localhost:8000/api/token/refresh/ with your refresh token and a new access token will be generated
for you. 

DEMO VIDEO
You can watch a demo video of this project on loom. Please visit the link 
https://www.loom.com/share/8404fd64d4244be2b50aaf7f678d4e9e


