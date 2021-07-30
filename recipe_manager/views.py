from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Recipe, RecipeIngredient, Ingredient, QuantityUnit, CurrencyUnit
from .forms import IngredientForm

def home(request):
	context = {
		'recipes': Recipe.objects.all(),
		'ingredients': Ingredient.objects.all(),
	}
	return render(request, 'recipe_manager/index.html', context)

def edit_ingredient(request, ingredient_id):
	ingredient = Ingredient()
	if ingredient_id > 0:
		ingredient = get_object_or_404(Ingredient, pk=ingredient_id)

	if request.method == 'POST':
		form = IngredientForm(request.POST)

		if form.is_valid():
			ingredient.name = form.cleaned_data['name']
			ingredient.quantity = form.cleaned_data['quantity']
			ingredient.currency = form.cleaned_data['currency']
			ingredient.save()

			return HttpResponseRedirect(reverse('home') )
	else:
		initial = {
			'name': ingredient.name,
			'quantity': ingredient.quantity,
			'currency': ingredient.currency,
		}
		form = IngredientForm(initial=initial)

	context = {
	'form': form,
	'ingredient': ingredient,
	}

	return render(request, 'recipe_manager/edit_ingredient.html', context)


def db_to_json(query):
	data = serializers.serialize('json', query)
	return HttpResponse(data, content_type='application/json')

def recipes(request):
	return db_to_json(Recipe.objects.all())

def ingredients(request):
	return db_to_json(Ingredient.objects.all())

def recipe_details(request):
	return db_to_json(RecipeIngredient.objects.all().select_related('ingredient'))

def quantity_unit(request):
	return db_to_json(QuantityUnit.objects.all().order_by('num_order'))

def currency_unit(request):
	return db_to_json(CurrencyUnit.objects.all().order_by('num_order'))