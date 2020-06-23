# Passing  OTL to user email account for inviting him in exam

## 1) Copy the code in the django server

## 2) Prepare some users' account as directed in https://github.com/amardrylab/django_adduser.git

## 3) Prepare your question paper in the file "otl/qp.dat".

## 4) Run the following command to generate question paper "question.html"

    cd otl
    python3 qp.py

## 5) Move the generated file in template folder

    cd ..
    mv otl/question.html template/

## 6) Run the following commands for sending emails
    ./manage.py shell
    >>>from otl.views import send_otl_email
    >>>send_otl_email()
    >>>exit()

## 7) Run the server

    ./manage.py runserver

## 4) Open any user account and click the link
