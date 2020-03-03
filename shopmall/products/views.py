from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products


# Create your views here.
def index(request):
    products = Products.objects.all()
    return render(request, 'products/index.html', {"products": products})


def show(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except:
        return redirect(index)

    return render(request, 'products/show.html', {"product": product})


def new(request):
    return None


def create(request):
    return None


def edit(request):
    return None


def update(request):
    return None


def destroy(request):
    return None
