from django.urls import path, include
from poll import views

app_name = 'poll'

urlpatterns=[
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('',views.index,name='index'),
]