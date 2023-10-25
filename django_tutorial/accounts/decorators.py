from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def print_user_permissions(request):
    group = ''
    if request.user.groups.exists():
                group = request.user.groups.all()[0].name

    return HttpResponse("User permissions printed in the consoledfs."+group)

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            
            #print_user_permissions(request)
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                user_permissions = request.user.user_permissions.all()
                pem = ''
                for permission in user_permissions:
                    pem = permission
                    print(permission)
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator