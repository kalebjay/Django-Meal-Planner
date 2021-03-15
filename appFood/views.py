from itertools import chain
import calendar
import random
import logging
logger = logging.getLogger(__name__)
from datetime import datetime, timedelta, date
from django.db import models, transaction, IntegrityError
from django.db.models import F, Count, Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from . utils import sortPieData
from . calendar import Calendar
from . models import StorageItem, Recipe, Ingredient, Meal
from . forms import StorageItemForm, RecipeForm, IngredientForm, MealForm
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)


############################################################################
# Home Page

class HomeView(TemplateView):
    template_name = 'appFood/home.html'

###########################################################################
# Storage Items

class StorageItemListView(ListView):
    model = StorageItem

def getShoppingList(request):
    low_items_List_queryset = StorageItem.objects.filter(quant_onHand__lt=1)
    need_list_queryset = Ingredient.objects.exclude(ingredient_name__in=list(StorageItem.objects.all()))
    shoppingList = list(chain(low_items_List_queryset, need_list_queryset))

    return render(request, 'appFood/shopping_list.html', {'shoppingList': shoppingList})

class StorageItemDetailView(DetailView):
    model = StorageItem

class CreateStorageItemView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/storageitem_detail.html'

    form_class = StorageItemForm
    model = StorageItem

class UpdateStorageItemView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/storageitem_detail.html'

    form_class = StorageItemForm
    model = StorageItem

class DeleteStorageItemView(LoginRequiredMixin, DeleteView):
    model = StorageItem
    success_url = reverse_lazy('storageitem_list')

##########################################################################
# Recipes

class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

class CreateRecipeView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/recipe_detail.html'

    form_class = RecipeForm
    model = Recipe

class UpdateRecipeView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/recipe_detail.html'

    form_class = RecipeForm
    model = Recipe

def decreaseStorage(request, pk):
    try:
        recipe = get_object_or_404(Recipe, pk=pk)
        ingredients = Ingredient.objects.select_related().filter(recipe = recipe)
        StorageItem.objects.filter(item_name__in=list(ingredients)).update(quant_onHand=F('quant_onHand')-1)
        StorageItem.objects.filter(item_name__in=list(ingredients)).update(item_count=F('item_count')+1)
    except IntegrityError:
        HttpResponse("Error, not enough items in storage.")

    return render(request, 'appFood/recipe_detail.html', {'recipe': recipe})


class DeleteRecipeView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')

###########################################################################
# Ingredients

class IngredientListView(ListView):
    model = Ingredient

class IngredientDetailView(DetailView):
    model = Ingredient

class CreateIngredientView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/ingredient_detail.html'

    form_class = IngredientForm
    model = Ingredient

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'appFood/ingredient_detail.html'

    form_class = IngredientForm
    model = Ingredient

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = reverse_lazy('recipe_list')

##########################################################################
#Calendar and Meals

class CalendarView(ListView):
	model = Meal
	template_name = 'appFood/calendar.html'
	success_url = reverse_lazy("calendar")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		d = get_date(self.request.GET.get('month', None))
		cal = Calendar(d.year, d.month)
		html_cal = cal.formatmonth(withyear=True)
		context['calendar'] = mark_safe(html_cal)
		context['prev_month'] = prev_month(d)
		context['next_month'] = next_month(d)
		return context

def get_date(month):
    if month:
        year, month = (int(x) for x in month.split('-'))
        return date(year, month, day = 1)
    return date.today()

def prev_month(d):
    first = d.replace(day = 1)
    prev_month = first - timedelta(days = 1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day = days_in_month)
    next_month = last + timedelta(days = 1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def meal(request, meal_id = None):
    instance = Meal()
    if meal_id:
        instance = get_object_or_404(Meal, pk=meal_id)
    else:
        instance = Meal()

    form = MealForm(request.POST or None, instance = instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'appFood/meal.html', {'form': form})

#############################################################################
# Reports

class ReportView(TemplateView):
    template_name = 'appFood/reports.html'

# Most used storage items
def topTenItems(request):
    return render(request, 'appFood/topTenStorage.html')

def topItemsChart(request):
    labels = []
    data = []
    topItems = StorageItem.objects.values('item_name', 'item_count').order_by('-item_count')[:10]
    for item in topItems:
        labels.append(item['item_name'])
        data.append(item['item_count'])

    return JsonResponse(data={'labels':labels, 'data':data,})

# Ingredients that overlap with other recipes the most
def mostCommonIngredients(request):
    return render(request, 'appFood/topTenIngred.html')

def topIngredsChart(request):
    labels = []
    data = []
    ingredients = Ingredient.objects.values('ingredient_name').annotate(count=Count('recipe')).filter(count__gte=2).order_by('-count')[:10]
    for ingred in ingredients:
        labels.append(ingred['ingredient_name'])
        data.append(ingred['count'])

    return JsonResponse(data={'labels':labels, 'data':data,})

# Gets all recipes by category
def recipeByCategory(request):
    labels = ['American', 'Italian', 'Mexican', 'Asian', 'Dessert', 'Other']
    data = []
    pieData = list(Recipe.objects.values('category_name').order_by('category_name').annotate(count=Count('category_name')))
    data = sortPieData(pieData)

    return render(request, 'appFood/recipeByCategory.html', {'labels': labels, 'data': data})

# Recipe recommendations
def recommendRecipes(request):
    recipes = list(Recipe.objects.all())
    randomeRecipes = random.sample(recipes, 3)
    meals = Meal.objects.all()
    toprecipes = Recipe.objects.prefetch_related('recipes').annotate(count=Count('recipes')).filter(count__gte=1).order_by('-count')[:2]
    bottomrecipes = Recipe.objects.prefetch_related('recipes').annotate(count=Count('recipes')).filter(count__gte=1).order_by('count')[:2]
    recmdRcpList = list(chain(randomeRecipes, toprecipes, bottomrecipes))

    return render(request, 'appFood/recommendedRecipes.html', {'recmdRcpList': recmdRcpList})
