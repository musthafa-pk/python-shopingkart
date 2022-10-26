from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})
def productspage(request):
    productspage =Product.objects.all()
    return render(request,'productspage.html',{'products':productspage})

def about(request):
    return HttpResponse("welcome to about page")

def contact(request):
    return HttpResponse("welcome to contact page")
