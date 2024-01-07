
# python -m venv venv
# source venv/Scripts/activate
# pip install django
# python freeze
# pip freeze > requirements.txt
# django-admin startproject my_pjt .
# python manage.py startapp my_app
# python manage.py runserver 

from django.urls import path
from my_app.views import hello

urlpatterns = [
    path('hello/', hello, name='hello'),
]