from django.shortcuts import render
from userauths.forms import UserRegisterForm



def register_view(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        print(form.data)
        if form.is_valid():
            print(form.username)
    else:
        form = UserRegisterForm()

    context = {
        'form' : form,
    }
    
    return render(request,'userauths/sign-up.html',context)