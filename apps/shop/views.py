from django.shortcuts import render, get_object_or_404
from .models import Author

def author_detail(request):
    pass

def index(request):
    return render(request, "public/index.html")

