from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, RecipeIngredient, Ingredient, QuantityUnit, CurrencyUnit

def recipes(request):
	data = serializers.serialize('json', Recipe.objects.all())
	return HttpResponse(data, content_type='application/json')

def ingredients(request):
	data = serializers.serialize('json', Ingredient.objects.all())
	return HttpResponse(data, content_type='application/json')

def recipe_details(request):
	data = serializers.serialize('json', RecipeIngredient.objects.all().select_related('ingredient'))
	return HttpResponse(data, content_type='application/json')

def quantity_unit(request):
	data = serializers.serialize('json', QuantityUnit.objects.all())
	return HttpResponse(data, content_type='application/json')

def currency_unit(request):
	data = serializers.serialize('json', CurrencyUnit.objects.all())
	return HttpResponse(data, content_type='application/json')