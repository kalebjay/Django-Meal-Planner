from django import forms
from django.forms import DateInput
from appFood.models import StorageItem, Recipe, Ingredient, Meal

class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = '__all__'

        widgets = {
            'start_time': DateInput(attrs = {'type': 'datetime-local'}, format ='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)

        self.fields['start_time'].input_formats = {'%Y-%m-%dT%H:%M',}

class StorageItemForm(forms.ModelForm):

    class Meta:
        model = StorageItem
        exclude = ('item_count',) # Used for reporting purposes, most used items

        widgets = {
            'item_name' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'storage_type' : forms.Select(attrs={'class': 'choiceselectclass'}),
            'container_type' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'quant_onHand' : forms.NumberInput(attrs={'class': 'numberinputclass'}),
            'quant_amount' : forms.NumberInput(attrs={'class': 'numberinputclass'}),
        }

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

        widgets = {
            'recipe_name' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'directions' : forms.Textarea(attrs={'class': 'textareaclass'}),
            'category_name' : forms.Select(attrs={'class': 'choiceselectclass'}),
        }

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('ingredient_name', 'measurement_units', 'measurement_quantity', 'recipe',)

        widgets = {
            'ingredient_name' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'measurement_units' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'measurement_quantity' : forms.TextInput(attrs={'class': 'textinputclass'}),
        }
