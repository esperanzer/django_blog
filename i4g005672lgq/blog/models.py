from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime  

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text= models.TextField()
    content = models.TextField()
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey("Author",on_delete=models.CASCADE)
    class Meta:
        abstract = True
    def get_user_model():
        return get_user_model().objects.get_or_create(username='deleted')[0]
