from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"index.html")

def category (request):
    return render(request,"category.html")

def about (request):
    return render(request,"about.html")

def product (request):
    return render(request,"product.html")


def contact (request):
    return render(request,"contact.html")


def contact (request):
    return render(request,"contact.html")


def contact (request):
    return render(request,"contact.html")


def login (request):
    return render(request,"login.html")


def register (request):
    return render(request,"register.html")