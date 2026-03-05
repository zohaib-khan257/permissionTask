from django.urls import path
from .import views

urlpatterns = [
    path("",views.PostList.as_view(),name="list"),
    path("create/",views.CreatePost.as_view(),name="create-post"),
    path("view/<int:id>",views.DetailPost.as_view(),name="detail-post"),
    path("update/<int:id>",views.UpdatePost.as_view(),name="update-post"),
    path("delete/<int:id>",views.DeletePost.as_view(),name="delete-post"),
    path("singup/",views.Signup.as_view(),name="signup"),
    path("loginup/",views.Login.as_view(),name="login"),
    path("logout/",views.Logout.as_view(),name="logout"),
] 