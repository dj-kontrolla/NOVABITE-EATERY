from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import MenuItem


def home(request):
    menu_items = MenuItem.objects.filter(available=True)

    return render(request, 'restaurant/home.html', {
        'menu_items': menu_items
    })