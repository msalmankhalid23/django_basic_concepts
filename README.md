# django_basic_concepts
Learning Django python basic concpets
1- Install Django
2- Access the admin panel
3- Create users and groups
4- Assign roles to either groups or users
5- Create separate apps e.g accounts
6- Create views
7- Define URL patterns
8- Create Models
9- Write decorators
10-Use Decorators for example to restrict the acccess 
    -on particular view
    -on specific buttons etc
    
**Installation Guide**
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
