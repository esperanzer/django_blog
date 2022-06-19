from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime  

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text= models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.TextField()
    # author = models.ForeignKey("User",on_delete=models.SET_NULL,null=True,related_name='posts')
    # user = models.ForeignKey(
    #     get_user_model(),
    #     null=True, 
    # )
