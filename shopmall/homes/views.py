from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm


def index(request):
    return render(request, 'homes/index.html')


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homes:index')
    return render(request, 'homes/register.html', {'form': form})
