from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.core.exceptions import PermissionDenied
# Create your views here.

class Signup(CreateView):
    model=Post
    form_class=CustomUserCreationForm
    template_name='myproject/signup.html'
    success_url=reverse_lazy('login')
    
class Login(LoginView):
    template_name="myproject/login.html"    

class Logout(LogoutView):
    next_page=reverse_lazy("list")    


class PostList(View):
    def get(self,request):
        model=Post.objects.all()
        return render(request,"myproject/post-lists.html",{
            "post_model":model,
        })      
        
class CreatePost(LoginRequiredMixin, View):
    def get(self, request):
        model_form = PostForm()
        return render(request, "myproject/create-post.html", {
            "model_form": model_form,
        })

    def post(self, request):
        model_form = PostForm(request.POST, request.FILES)
        if model_form.is_valid():
            post = model_form.save(commit=False) 
            post.created_by = request.user
            post.save()                           
            return redirect('list')
        return render(request, "myproject/create-post.html", {
            "model_form": model_form,
        })
        
class DetailPost(View):
    def get(self,request,id)     :
        post_model=Post.objects.get(pk=id)
        return render(request,"myproject/detail-post.html",{
            "models":post_model,
        })   
            
class UpdatePost(LoginRequiredMixin,View):
    def get(self,request,id)     :
        post_model=Post.objects.get(pk=id)
        if  post_model.created_by != request.user:
            raise PermissionDenied
            
        model_form=PostForm(instance=post_model)
        return render(request,"myproject/update-post.html",{
            "models":post_model,
            "model_form":model_form,
        })   
    
    def post(self,request,id):
        post_model=Post.objects.get(pk=id)
        
        if  post_model.created_by != request.user:
            raise PermissionDenied       
        
        model_form=PostForm(request.POST,instance=post_model)
        if model_form.is_valid():
            model_form.save()
            return redirect("list")
        return render(request,"myproject/update-post.html",{
            "models":post_model,
            "model_form":model_form,
        })       
        
class DeletePost(View):
    def get(self,request,id)     :
        post_model=Post.objects.get(pk=id)
        if not request.user.is_superuser:
            raise PermissionDenied
        return render(request,"myproject/delete-post.html",{
            "models":post_model,
        })   
    
    def post(self,request,id):
        post_model=Post.objects.get(pk=id)
        if not request.user.is_superuser:
            raise PermissionDenied
        post_model.delete()
        return redirect("list")     

           