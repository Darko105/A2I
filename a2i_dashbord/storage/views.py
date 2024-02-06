from django.shortcuts import render
from .models import Product
from django.db.models import Q

# Create your views here.


def storage_view(request):
    
    admin = request.session['userIsAdmin'] 
    name  = request.session['username'] 
    bio = request.session['bio']
    
    if request.method == 'POST':
        searched = request.POST['searchProd']
        product = Product.objects.filter(
            Q(name__contains = searched)|
            Q(discription__contains = searched))
        print(product)
        oddEven = 1
    
        context = {
                'product' : product,
                'oddEven' : oddEven,
                'name' : name,
                'admin' : admin,
                'bio' : bio,
        }
        return render(request,'storage/storage.html',context)
    else:
        product = Product.objects.all()
        return render(request,'storage/storage.html',{'empty':product})



def edit_view(request,name):
    print(name)
    context = {
        'name' : name,
    }
    return render(request,'storage/edit.html',context)
    
    
