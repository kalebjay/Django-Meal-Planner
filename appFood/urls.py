from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('shoppingList', views.getShoppingList, name='shopping_list'),
#   Calendar
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('meal/new/', views.meal, name='meal_new'),
    path('meal/<int:meal_id>/edit/', views.meal, name='meal_edit'),
#   Storage Items
    path('storageitem/', views.StorageItemListView.as_view(), name='storageitem_list'),
    path('storageitem/<int:pk>', views.StorageItemDetailView.as_view(), name='storageitem_detail'),
    path('storageitem/new', views.CreateStorageItemView.as_view(), name='storageitem_new'),
    path('storageitem/<int:pk>/edit/', views.UpdateStorageItemView.as_view(), name='storageitem_edit'),
    path('storageitem/<int:pk>/remove/', views.DeleteStorageItemView.as_view(), name='storageitem_remove'),
    path('<int:pk>/update', views.decreaseStorage, name='storage_decrease'),
#   Recipes
    path('recipe/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/new', views.CreateRecipeView.as_view(), name='recipe_new'),
    path('recipe/<int:pk>/edit/', views.UpdateRecipeView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/remove/', views.DeleteRecipeView.as_view(), name='recipe_remove'),
#   Ingredients
    path('ingredient/', views.IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name='ingredient_detail'),
    path('ingredient/new', views.CreateIngredientView.as_view(), name='ingredient_new'),
    path('ingredient/<int:pk>/edit/', views.UpdateIngredientView.as_view(), name='ingredient_edit'),
    path('ingredient/<int:pk>/remove/', views.DeleteIngredientView.as_view(), name='ingredient_remove'),
#   Reports
    path('report/', views.ReportView.as_view(), name='reports'),
    path('topstorage/', views.topTenItems, name='top_items'),
    path('topItemsChart/', views.topItemsChart, name='topItemsChart'),
    path('topingred/', views.mostCommonIngredients, name='top_ingred'),
    path('topIngredsChart/', views.topIngredsChart, name='topIngredsChart'),
    path('recipebycategory/', views.recipeByCategory, name='recipe_by_category'),
    path('recommendedRecipes/', views.recommendRecipes, name='recommendedRecipes'),
]
