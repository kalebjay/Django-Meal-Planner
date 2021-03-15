from django.contrib import admin
from appFood.models import StorageItem, Recipe, Ingredient, Meal

# Register your models here.
admin.site.register(Meal)
admin.site.register(StorageItem)
admin.site.register(Recipe)
admin.site.register(Ingredient)
