from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Products
from .forms import ProductForm


def index(request):
    products = Products.objects.all()
    return render(request, 'products/index.html', {"products": products})


def show(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except:
        return redirect('products:index')

    return render(request, 'products/show.html', {"product": product})


def new(request):
    form = ProductForm()
    return render(request, 'products/new.html', {"form": form})


def create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products:index')
    return render(request, 'products/new.html', {"form": form})


def update(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products:show', product_id=product_id)
    return render(request, 'products/edit.html', {'form': form})


def destroy(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.POST:
        product.delete()
        return redirect('products:index')
    return render(request, 'products/destroy.html', {'object': product})
