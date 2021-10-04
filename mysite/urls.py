

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', include('blog.urls')),
    path('', TemplateView.as_view(template_name='blog/registration/home.html'), name='home'),
    path('blog/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    
    path('poll/', include('poll.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)