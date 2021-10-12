from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def image(request):
    images = News.objects.all()
    return render(request, 'index.html', {'images': images})
