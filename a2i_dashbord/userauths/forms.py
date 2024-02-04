from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterForm(UserCreationForm):
  
    class Meta:
        model = User
        fields = ['username','email']