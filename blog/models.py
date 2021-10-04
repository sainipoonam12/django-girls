from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
# from taggit.managers import TaggableManager 
from django.utils import timezone
from django.conf import settings
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, null=True)

	def __str__(self):
		return self.name
		
class Tag(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, null=True)
	text=  models.TextField(max_length=200)

	def __str__(self):
		return self.name


class MyUser(AbstractUser):
	mobile_number = models.CharField(max_length=10)
	profile_img= models.ImageField(upload_to='images',null=True,blank=True)
	email = models.EmailField(('email'), unique = False)

	def __str__(self):
		return self.username
	
class Post(models.Model):
	author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from='title', max_length = 200, editable=False,unique=True)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='posts')
	tags = models.ManyToManyField(Tag)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog')

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True,related_name='replies')
	

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.name)

