# Opendrive
Opensource is a self hosted file hosting system.

#Prerequisites

Operating system
>mac,

>linux

Database
>sqlite3

Languages Used
>Python,

>Angularjs

ORM Used
>SQLAlchemy

Python packages used

>flask,

>flask-admin,

>sqlalchemy,

>enum,

>requests,

>flask-login


#Installation 
Create a virtualenv

>virtualenv venv

Activate virtualenv

>source venv/bin/activate

Install python packages using setup.py, run the following command

>python setup.py

Once this is done, using models build the db and place the file in crud folder using the following commands

>python models/models.py

Move the file from db model from models to crud

>mv opendrive.db ../crud/

After this, we are ready to use the tool run the following command

>python app.py

This will run the server on port number 5000,open browser and search for http://localhost:5000 


#Endpoints and descriptions

Filename app.py

functions

    deletefile(*args, **kwargs)
        Function to delete a file by fileid

    getfile(*args, **kwargs)
        Function to check access of a user to a given function.

    loginauthorisation()
        Function to authorise a username and password against the credentials
        present in the database and redirect the user to home page.

    logoutpage(*args, **kwargs)
        Function to logout user and redirect them to the login page.

    newfileupload(*args, **kwargs)
        function to upload user to server.

    onboardingpage()
        Function to render the onboarding page.

    onboardingpagewithnotification(notification)
        Function to render a login page with a notification

    register_user()
        Function to onboard the user on to the application.

    render_registrationpage()
        Function to render the register page where the user is onboarded.

    render_searchpage(*args, **kwargs)
        Function to render the search page.

    returnfiles(*args, **kwargs)
        Function to return list of files uploaded by the user.

Filename app.py

functions

    addfile(fileid, actualfilename, currentuser)
        Function to store file data in db.


Filename read.py

functions

    check_access(fileid, currentuser)
        Function to check users access to the requested file.

    listofilesuploaded(currentuser)
        Function to return list of files uploaded by a user.

Filename: delete.py

functions
    deletefile(fileid, currentuser)
        Function to delete filedata from the database.


#Navigating through the application

#webpages

url:'/'-This is the login and registration page you can signup or sign in to the platform using this page

url:'/home'-This page has features to add, delete and download the files the users have uploaded

#features

login: enter username and password to login to the application

logout: click on logout button at the bottom on the left pane

upload: click on an upload button and upload mulitple files at once

delete: right click on the file to get delete option

download:to download the file click on the download button below the file


#Development Log
Access development log at https://tymline.co/ramharsha/opendrive

#scope of improvement
please raise issues or request feature changes via the issues section in github

#contact details
For any further queries you can mail me on kunchamharsha@gmail.com,
you can also raise an issue and I will get back to you as soon as possible
