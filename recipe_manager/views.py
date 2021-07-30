from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Recipe, RecipeIngredient, Ingredient, QuantityUnit, CurrencyUnit

def db_to_json(query):
	data = serializers.serialize('json', query)
	return HttpResponse(data, content_type='application/json')

def recipes(request):
	context = {
		'recipes': Recipe.objects.all(),
	}
	return render(request, 'recipe_manager/index.html', context)

def ingredients(request):
	return db_to_json(Ingredient.objects.all())

def recipe_details(request):
	return db_to_json(RecipeIngredient.objects.all().select_related('ingredient'))

def quantity_unit(request):
	return db_to_json(QuantityUnit.objects.all().order_by('num_order'))

def currency_unit(request):
	return db_to_json(CurrencyUnit.objects.all().order_by('num_order'))