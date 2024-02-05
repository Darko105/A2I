from django.shortcuts import render
from .models import Product
from django.db.models import Q

# Create your views here.


def storage_view(request):
    
    if request.method == 'POST':
        searched = request.POST['searchProd']
        product = Product.objects.filter(
            Q(name__contains = searched)|
            Q(discription__contains = searched))
        print(product)
        oddEven = 1
    
        context = {
                'product' : product,
                'oddEven' :oddEven
        }
        return render(request,'storage/storage.html',context)
    else:
        product = Product.objects.all()
        return render(request,'storage/storage.html',{'empty':product})
    
    
