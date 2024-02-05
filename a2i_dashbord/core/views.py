from django.shortcuts import render
from userauths.models import User

# Create your views here.
def index(request):
    
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            admin = True
        else:
            admin = False
        
        if request.user.is_authenticated:
            name = request.user.username
            bio = request.user.bio
            
            
        context = {
            'userIsAdmin' : admin,
            'username' : name,
            'bio' : bio
        }
        
        return render(request,'core/index.html',context)
    else:
        return render(request,'core/index.html',{})