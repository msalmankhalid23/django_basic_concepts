# django_basic_concepts
Learning Django python basic concpets

#install django
pip install django

#check Version
django-admin --version

#create the startup proejct
  django-admin startproject django_tutorial

#create the app:
  python manage.py startapp accounts

#run the django project: 
   python manage.py runserver

#create the db files
python manage.py migrate

#create super user to login on the admin panel
  python manage.py createsuperuser
  
#create models then run this command to create the migration
  python manage.py makemigrations
  python manage.py migrate


#Admin URL: and Login with SuperUser
http://127.0.0.1:8000/admin
