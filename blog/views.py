from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import *
from .models import Post, MyUser, Comment
from .forms import PostForm, Category
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from .forms import CommentForm
from django.views.generic.edit import CreateView, UpdateView
from .forms import MyUserCreationForm, MyUserChangeForm


def post_list(request,tag_slug=None):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts,})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	print(post.tags.all(), 'tagssssssssssssss')
	comments = post.comments.filter(parent__id=None,active=True)
	new_comment = None
	if request.method == "POST":
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_obj = None
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			if parent_id:
				parent_obj = Comment.objects.get(id=parent_id)
				if parent_obj:
					
					replay_comment = comment_form.save(commit=False)
					
					replay_comment.parent = parent_obj
					replay_comment.post = post
					replay_comment.save()
			else:
				new_comment = comment_form.save(commit=False)
				new_comment.post = post
				new_comment.save()
		comment_form = CommentForm()
	else:
		comment_form = CommentForm()
	return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments,'comment_form': comment_form})


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			form.save_m2m()
			return redirect('blog:post_detail', slug=post.slug)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})




def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			form.save_m2m()
			return redirect('blog:post_detail', slug=slug)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def tag_details(request,slug):
	tags= Tag.objects.filter(slug=slug).last()
	posts = Post.objects.filter(tags=tags)
	return render(request, 'blog/tag_details.html',{'posts':posts})

def tag_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tag_list.html',{'tags':tags})
	

def category(request):
	cats = Category.objects.all()
	return render(request, 'blog/category_list.html',{'category':cats})
	
def category_detail(request,slug):
	cat = Category.objects.filter(slug=slug).last()
	posts = Post.objects.filter(category=cat)
	return render(request, 'blog/category_detail.html',{'cats':posts})

class profile(TemplateView):
	model = MyUser
	success_url = reverse_lazy('login')
	template_name = 'blog/profile.html'
	def get_object(self):
		return self.request.user

class edit_profile(UpdateView):
	form_class = MyUserChangeForm
	success_url = reverse_lazy('blog:profile')
	template_name = 'blog/edit_profile.html'
	def get_object(self):
		return self.request.user

def signup(request):
	if request.method == 'POST':
		print(request.POST,'4343434343434')
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			print(form,'122212121212122')
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('blog:post_list')
	else:
		form = MyUserCreationForm()
	return render(request, 'blog/registration/signup.html', {'form': form})


def login1(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			print(user,'122122212')
			login(request, user)
			return redirect('blog:profile')
	  
	return render(request, 'blog/registration/login.html')


