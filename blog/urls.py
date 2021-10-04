from django.urls import path
from . import views
from .views import  UpdateView, edit_profile, profile


app_name = 'blog'

urlpatterns = [
    
    path('edit_profile/profile/blog/', edit_profile.as_view(), name='edit_profile'),
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('signup/blog/', views.signup, name='signup'),
    path('profile/blog/', profile.as_view(), name='profile'),
    path('login/blog/', views.login1, name='login'),
    path('post/new/', views.post_new, name='post_new'),
   
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('category_detail/<str:slug>/', views.category_detail, name='category_detail'),
    path('tag_details/<str:slug>/', views.tag_details, name='tag_details'),
    path('category/', views.category, name='category'),
    path('tag_list/',views.tag_list, name='tag_list'),
    path('', views.post_list, name='post_list'),
    
  
    

    
]
