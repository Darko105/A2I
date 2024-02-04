from django.shortcuts import render
from userauths.models import User

# Create your views here.
def index(request):
    
    if request.user.is_staff or request.user.is_superuser:
        admin = True
    else:
        admin = False
        
        
    context = {
        'userIsAdmin' : admin,
    }
    
    return render(request,'core/index.html',context)