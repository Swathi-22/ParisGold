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
    return render(request,'web/index.html',context)

def category(request):
    context = {

    }
    return render(request,'web/index.html',context)

def blog(request):
    context = {

    }
    return render(request,'web/index.html',context)

def blogDetails(request):
    context = {

    }
    return render(request,'web/index.html',context)

def gallery(request):
    context = {

    }
    return render(request,'web/index.html',context)

def contact(request):
    context = {

    }
    return render(request,'web/index.html',context)