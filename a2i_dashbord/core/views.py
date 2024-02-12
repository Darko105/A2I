from django.shortcuts import render,redirect
from userauths.models import User

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser:
            admin = True
        else:
            admin = False
        request.session['userIsAdmin'] = admin
        
        if request.user.is_authenticated:
            name = request.user.username
            bio = request.user.bio
            request.session['username'] = name
            request.session['bio'] = bio
            
        # Store data in session
        
        

        return redirect('storage:storage')
    else:
        return redirect('userauths:sign-up')