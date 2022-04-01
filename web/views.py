from importlib.resources import contents
from django.shortcuts import render,HttpResponse, get_object_or_404
from .forms import ContactForm
from .models import Gallery,Update,Contact
import json
from django.http import JsonResponse

 
# Create your views here.
def index(request):
    updates=Update.objects.all()

    context = {
        "updates":updates
    }
    return render(request,'web/index.html',context)


def about(request):
    gallery = Gallery.objects.all()
    updates=Update.objects.all()
    context = {
        "gallery":gallery,
        "updates":updates
    }
    return render(request,'web/about.html',context)


def gold(request):
    context = {

    }
    return render(request,'web/gold.html',context)


def diamond(request):
    context = {

    }
    return render(request,'web/diamond.html',context)


def blog(request):
    updates=Update.objects.all()
    context={
      
        "updates":updates,

    }
    return render(request,'web/blog.html',context)


def blogDetails(request,slug):
    update = get_object_or_404(Update,slug=slug)
    updates=Update.objects.all()
    context={
        'update':update,
        'updates':updates
        
    }
    return render(request,'web/blog-details.html',context)

def gallery(request):
    gallery = Gallery.objects.all()
    context={
        "gallery":gallery

    }
    return render(request,'web/gallery.html',context)


def contact_form(request):
    forms=ContactForm(request.POST or None)
    context={
        'forms':forms

    }
    return render(request,'web/contact.html',context)

def SaveContactForm(request):
  
    forms=ContactForm(request.POST or None)
    if request.method=='POST':
       
        print('success')
        if forms.is_valid():
           
            forms.save()
      
           
    return JsonResponse({'title':'y'})