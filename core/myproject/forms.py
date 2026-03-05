from .models import Post, User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'captions', 'image',)
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username']