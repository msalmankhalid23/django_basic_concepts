
from django.urls import path

from .decorators import print_user_permissions
from .views import home, customers, loginPage, register, logoutPage

urlpatterns = [

    path('', home, name='home'),
    path('customers/', customers, name='customers'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', register, name='register'),
    path('print_permissions/', print_user_permissions, name='print_user_permissions'),
]
