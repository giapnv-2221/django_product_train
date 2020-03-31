from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import Products, Categories
from .forms import ProductForm
from django.forms.models import inlineformset_factory
from django.views.generic.edit import CreateView, UpdateView

ProductFormset = inlineformset_factory(Categories, Products, fields=("name", "info", "price"))


class CategoryCreateView(CreateView):
    model = Categories
    fields = ("name",)
    template_name = "categories/category_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["products"] = ProductFormset(self.request.POST)
        else:
            data["products"] = ProductFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        products = context["products"]
        self.object = form.save()
        if products.is_valid():
            products.instance = self.object
            products.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("homes:index")


class CategoryUpdateView(UpdateView):
    model = Categories
    fields = ("name",)
    template_name = "categories/category_form.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["products"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            data["products"] = ProductFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        products = context["products"]
        self.object = form.save()
        if products.is_valid():
            products.instance = self.object
            products.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("homes:index")



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
