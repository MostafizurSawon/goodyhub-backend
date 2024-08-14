# GoodyHub-backend

## Backend Live: https://goodyhub-backend.onrender.com/

## Frontend Live: https://goodyhub.netlify.app/

## Frontend Github: https://github.com/MostafizurSawon/goodyhub-frontend

Short Description: This backend application is made with Django Rest Framework. 

    "products-list": "http://goodyhub-backend.onrender.com/products/products-list/",
    "category": "http://goodyhub-backend.onrender.com/products/category/",
    "reviews": "http://goodyhub-backend.onrender.com/products/reviews/"
    "users-list": "https://goodyhub-backend.onrender.com/user/list/",
    "users-register": "https://goodyhub-backend.onrender.com/user/register/",
    "users-login": "https://goodyhub-backend.onrender.com/user/login/",
    "users-logout": "https://goodyhub-backend.onrender.com/user/logout/"

An user can register with his email address. A verification email will be sent to user email. Unless he clicks on that verification link, account will not be activated. After email confirmation, the user will gain access to the website. Duplicate account with same email is not allowed.

A logged in user can add new category and products. They can also edit/delete their products. I also added pagination, add review, and search options in the backend.


# To run this project in local server, clone this repository and run this command:
- pip install -r requirements.txt
- py manage.py runserver

** Enviroment should be activated
