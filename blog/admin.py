from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Post, Comment, Category, Tag
from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
	add_form = MyUserCreationForm
	form = MyUserChangeForm
	model = MyUser
	list_display = ['username', 'mobile_number','email','profile_img',]
	fieldsets = UserAdmin.fieldsets + (
			(None, {'fields': ('mobile_number','profile_img')}),
	) 

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)


