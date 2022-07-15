from django.shortcuts import render, HttpResponse
from .models import Laptops

# Create your views here.


def homepage(request):
    return render(request, "index.html")


def laptop(request):
    laptop_object = Laptops.objects.get(id=1)
    description = f"{laptop_object.name}, {laptop_object.description}"
    return HttpResponse(description)

def categories(request):
    products = Laptops.objects.all()
    data = {"all_laptops": products}
    return render(request, "categories.html", context=data)