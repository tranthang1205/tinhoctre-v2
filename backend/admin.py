from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(Type)
admin.site.register(About)
admin.site.register(Food_Ingredient)
admin.site.register(Food_Type)
admin.site.register(Food_About)