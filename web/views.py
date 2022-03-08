from importlib.resources import contents
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request,'web/index.html',context)


def about(request):
    context = {

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
    context = {

    }
    return render(request,'web/blog.html',context)


def blogDetails(request):
    context = {

    }
    return render(request,'web/blog-details.html',context)


def gallery(request):
    context = {

    }
    return render(request,'web/gallery.html',context)


def contact(request):
    context = {

    }
    return render(request,'web/contact.html',context)