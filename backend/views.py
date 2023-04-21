from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, template_name='landing.html')

def home(request):
    return render(request, template_name='home.html')

def searchfood(request):
    return render(request, template_name='search-food.html')

def searchingredients(request):
    return render(request, template_name='search-ingredients.html')

def food(request):
    return render(request, template_name='food.html')
