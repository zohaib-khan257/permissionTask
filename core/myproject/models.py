from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    captions = models.TextField()
    image = models.ImageField(upload_to='media')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return self.title                                       
    
    
