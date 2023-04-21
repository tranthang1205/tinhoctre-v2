from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(_("Name"), max_length=50)

class Food(models.Model):
    about = models.TextField(_("Description"))
    # picture = models.ImageField(_("Image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    calo = models.FloatField(_("Calo"))
    time = models.TimeField(_("time"), auto_now=False, auto_now_add=False)
    ings = models.ManyToManyField(Ingredient, verbose_name=_("nguyen lieu"), through='Food_Ingredient')

class Food_Ingredient(models.Model):
    food_id = models.ForeignKey(Food, verbose_name=_("food"), on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, verbose_name=_("ingredient"), on_delete=models.CASCADE)