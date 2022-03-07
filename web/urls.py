from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('category/', views.category,name='category'),
    path('blog/', views.blog,name='blog'),
    path('blog-details/', views.blogDetails,name='blogDetails'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
]