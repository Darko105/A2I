from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length = 50,null = False)
    discription = models.TextField(max_length = 500, null=True)
    local = models.CharField(max_length = 10,null = True)
    position = models.CharField(max_length = 10,null = True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
