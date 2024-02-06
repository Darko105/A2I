from django.urls import path
from storage import views


app_name = 'storage'

urlpatterns = [
    path('storage/',views.storage_view,name='storage'),
    path('storage/edit/<str:name>/',views.edit_view,name='edit_view')
    
]