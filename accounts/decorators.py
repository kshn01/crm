from django.http import HttpResponse
from django.shortcuts import redirect

# ----- REFERENCE(WRAPPER)
# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else: 
# ----- 


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # print('working', allowed_roles) #checking the function execution
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1 style="text-align: center;">Un-Authorized</h1>')
        return wrapper_func
    return decorator