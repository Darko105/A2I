from django.shortcuts import render
from .models import Product
from django.db.models import Q

def storage_view(request):
    admin = request.session['userIsAdmin'] 
    name = request.session['username'] 
    bio = request.session['bio']
    
    if request.method == 'POST':
        searched = request.POST['searchProd']
        search_terms = searched.split()  # Split the input into separate words

        # Search for the combination of words
        combined_query = Q()
        for term in search_terms:
            combined_query &= (Q(name__icontains=term) | Q(discription__icontains=term) | Q(date__icontains=term))

        product_combined = Product.objects.filter(combined_query)

        if product_combined.exists():
            # If results are found for the combination of words, use them
            product = product_combined
        else:
            # If no results, search for each word individually
            individual_query = Q()
            for term in search_terms:
                individual_query |= Q(name__icontains=term) | Q(discription__icontains=term) | Q(date__icontains=term)

            product = Product.objects.filter(individual_query)

        # Order the products by date
        product = product.order_by('date')

        oddEven = 1
    
        context = {
            'product': product,
            'oddEven': oddEven,
            'name': name,
            'admin': admin,
            'bio': bio,
            'search' : searched,
        }
        return render(request, 'storage/storage.html', context)
    else:
        # Order all products by date
        product = Product.objects.all().order_by('date')
        return render(request, 'storage/storage.html', {'empty': product})


def edit_view(request, name):
    print(name)
    context = {
        'name': name,
    }
    return render(request, 'storage/edit.html', context)
