from django.urls import path
from userauths import views
from django.contrib.auth.views import LogoutView


app_name = 'userauths'

urlpatterns = [
    path('sign-up/',views.register_view,name='sign-up'),
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
]
