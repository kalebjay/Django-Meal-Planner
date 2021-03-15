from django.db import models
from django.urls import reverse
import datetime

######################################################################
# Storage/Inventory section

class StorageItem(models.Model):
    PANTRY = 1
    FRIDGE = 2
    FREEZER = 3
    LOCALE = (
        (PANTRY, ('Room temp storage')),
        (FRIDGE, ('Fridge - cold storage')),
        (FREEZER, ('Freezer - really cold storage')),
    )

    item_name = models.CharField(max_length=250)
    storage_type = models.PositiveSmallIntegerField(choices = LOCALE, default = PANTRY,)
    container_type = models.CharField(max_length=50, default = 'null')
    quant_onHand = models.PositiveIntegerField(default=0)
    quant_amount = models.DecimalField(max_digits=5, decimal_places=2)
    item_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['item_name']

    def get_absolute_url(self):
        return reverse("storageitem_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.item_name

##########################################################################
# Recipe section

class Recipe(models.Model):
    MAIN_DISH = 1
    BREAKFAST = 2
    LUNCH = 3
    SOUPS  = 4
    AMERICAN = 5
    ITALIAN = 6
    MEXICAN = 7
    ASIAN = 8
    RUSSIAN = 9
    EUROPEAN = 10
    DESSERTS = 11
    OTHER = 12

    CATEGORIES = (
        (MAIN_DISH, ('Main dishes')),
        (BREAKFAST, ('Breakfast')),
        (LUNCH, ('Lunch')),
        (SOUPS, ('Soups')),
        (AMERICAN, ('American or home style meals')),
        (ITALIAN, ('Italian')),
        (MEXICAN, ('Mexican')),
        (ASIAN, ('Asian, Chinese, Japanese, etc')),
        (RUSSIAN, ('Russian')),
        (EUROPEAN, ('European, any country')),
        (DESSERTS, ('Desserts and treats')),
        (OTHER, ('Other, anything')),
    )

    recipe_name = models.CharField(max_length=200)
    directions = models.TextField(max_length=3000)
    category_name = models.PositiveSmallIntegerField(choices = CATEGORIES, default = MAIN_DISH)

    class Meta:
        ordering = ['recipe_name']

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.recipe_name

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=250)
    measurement_units = models.CharField(max_length=50)
    measurement_quantity = models.CharField(max_length=50)
    recipe = models.ManyToManyField(Recipe, related_name='ingredients')

    class Meta:
        ordering = ['ingredient_name']

    def get_absolute_url(self):
        return reverse("ingredient_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.ingredient_name

#########################################################################
# Calendar section

class Meal(models.Model):
    start_time = models.DateTimeField(default=datetime.date.today)
    recipe = models.ForeignKey(Recipe, related_name='recipes', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.recipe)

    @property
    def get_html_url(self):
        url = reverse('meal_edit', args=(self.id,))
        return f'<a href="{url}"> {self.recipe} </a>'
