from django.urls import path
from storage import views


app_name = 'userauths'

urlpatterns = [
    path('storage/',views.storage_view,name='storage')
    
]