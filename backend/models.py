from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    # đơn vị đo lường
    measure = models.CharField(_("Measure"), max_length=50)

class Type(models.Model):
    name = models.CharField(_("Name"), max_length=50)

class About(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    step = models.TextField(_("Step"))
    picture = models.ImageField(_("picture"), upload_to="about", null=True)

class Food(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    calo = models.FloatField(_("Calo"))
    time = models.CharField(_("Time"), max_length=50)
    introduce = models.TextField(_("Introduce"))
    number_of_ingredients = models.IntegerField(_("number_of_ingredients"))
    picture = models.ImageField(_("picture"), upload_to="Food")
    # liên kết giữa 2 bảng, chỉ cần 1 liên kết là tạo được liên thông   
    ings1 = models.ManyToManyField(Ingredient, verbose_name=_("nguyen lieu"), through='Food_Ingredient')
    ings2 = models.ManyToManyField(Type, verbose_name=_("loai nguyen lieu"), through='Food_Type')
    ings3 = models.ManyToManyField(About, verbose_name=_("cac buoc nau"), through="Food_About")

class Food_Ingredient(models.Model):
    food_id = models.ForeignKey(Food, verbose_name=_("food"), on_delete=models.CASCADE, related_name='ingredient')
    ingredient_id = models.ForeignKey(Ingredient, verbose_name=_("ingredient"), on_delete=models.CASCADE)
    amount = models.CharField(_("Amount"), max_length=50)

class Food_Type(models.Model):
    food_id = models.ForeignKey(Food, verbose_name=_("food"), on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, verbose_name=_("type"), on_delete=models.CASCADE, related_name='type')

class Food_About(models.Model):
    food_id = models.ForeignKey(Food, verbose_name=_("food"), on_delete=models.CASCADE)
    about_id = models.ForeignKey(About, verbose_name=_("about"), on_delete=models.CASCADE, related_name='about')