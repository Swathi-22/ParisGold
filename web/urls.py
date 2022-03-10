from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('gold/', views.gold,name='gold'),
    path('diamond/', views.diamond,name='diamond'),
    path('blog/', views.blog,name='blog'),
    path('blog-details/<str:slug>/', views.blogDetails,name='blogDetails'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
    path('SaveContactForm/', views.SaveContactForm,name='SaveContactForm'),
    
]