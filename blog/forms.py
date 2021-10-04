from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Post,Comment, Category
from django import forms
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = MyUser
        fields = ('username', 'mobile_number','email',)

class MyUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = MyUser
        fields = ('username', 'mobile_number','email','profile_img')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category', 'tags')

        # widgets = {
        #     'Category' : forms.Select(choices=choices,attrs={'class': 'form-control'}),

        # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


        

