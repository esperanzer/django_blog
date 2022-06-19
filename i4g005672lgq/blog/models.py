from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text= models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    # author = models.ForeignKey("User",on_delete=models.SET_NULL,null=True,related_name='posts')
    # user = models.ForeignKey(
    #     get_user_model(),
    #     null=True, 
    # )

# Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.