from django.shortcuts import render
from backend.models import *

# Create your views here.

def landing(request):
    return render(request, template_name='landing.html')

def home(request):
    return render(request, template_name='home.html')

def searchfood(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')
        foods = Food.objects.filter(name__icontains=keyword)
        ct = {'foods': foods}
        return render(request, 'search-food.html', ct)
    return render(request, 'search-food.html')

def searchingredients(request):
    return render(request, template_name='search-ingredients.html')

def food(request):
   foods = Food.objects.all()
   ct = {"foods": foods} 
   return render(request, 'food.html', ct)
    