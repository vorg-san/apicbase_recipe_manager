from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import models 
from . import forms

def home(request):
	context = {
		'recipes': models.Recipe.objects.all(),
		'ingredients': models.Ingredient.objects.all(),
	}
	return render(request, 'recipe_manager/index.html', context)

def edit_ingredient(request, ingredient_id):
	ingredient = models.Ingredient()
	initial_form = {}

	if ingredient_id > 0:
		ingredient = get_object_or_404(models.Ingredient, pk=ingredient_id)
		initial_form = {
			'name': ingredient.name,
			'article': ingredient.article,
			'quantity': ingredient.quantity,
			'currency': ingredient.currency,
			'currencyUnit': ingredient.currencyUnit,
			'quantityUnit': ingredient.quantityUnit,
		}

	if request.method == 'POST':
		form = forms.IngredientForm(request.POST)

		if form.is_valid():
			ingredient.name = form.cleaned_data['name']
			ingredient.article = form.cleaned_data['article']
			ingredient.quantity = form.cleaned_data['quantity']
			ingredient.currency = form.cleaned_data['currency']
			ingredient.currencyUnit = form.cleaned_data['currencyUnit']
			ingredient.quantityUnit = form.cleaned_data['quantityUnit']
			ingredient.save()

			return HttpResponseRedirect(reverse('recipe_manager:home') )
	else:
		form = forms.IngredientForm(initial=initial_form)

	context = {
	'form': form,
	'ingredient': ingredient,
	}

	return render(request, 'recipe_manager/edit_ingredient.html', context)

def edit_recipe(request, recipe_id):
	recipe = models.Recipe()
	initial_name_form = {}

	if recipe_id > 0:
		recipe = get_object_or_404(models.Recipe, pk=recipe_id)
		initial_name_form = {
			'name': recipe.name,
		}

	if request.method == 'POST':
		if request.POST['objective'] == 'saveName':
			form_ingredient = forms.RecipeIngredientForm()
			form_name = forms.RecipeNameForm(request.POST)
	
			if form_name.is_valid():
					recipe.name = form_name.cleaned_data['name']
					recipe.save()			
					
					return HttpResponseRedirect(reverse(f'recipe_manager:edit recipe', kwargs={'recipe_id':recipe.id}))
		else:
			form_name = forms.RecipeNameForm(initial=initial_name_form)
			form_ingredient = forms.RecipeIngredientForm(request.POST)
	
			if form_ingredient.is_valid():
					recipe_list = models.RecipeList()
					recipe_list.recipe = recipe
					recipe_list.quantity = form_ingredient.cleaned_data['quantity']
					recipe_list.ingredient = get_object_or_404(models.Ingredient, pk=form_ingredient.cleaned_data['ingredient'].id)
					recipe_list.save()
					recipe.ingredients.add(form_ingredient.cleaned_data['ingredient'])
					# recipe.save()				

			# return HttpResponseRedirect(reverse('recipe_manager:home') )
	else:
		form_name = forms.RecipeNameForm(initial=initial_name_form)
		form_ingredient = forms.RecipeIngredientForm()

	context = {
	'form_name': form_name,
	'form_ingredient': form_ingredient,
	'recipe': recipe,
	}

	return render(request, 'recipe_manager/edit_recipe.html', context)


# BELOW WOULD BE USED ONLY FOR INTEGRATION WITH PURE JS FRAMEWORK LIKE REACT

def db_to_json(query):
	data = serializers.serialize('json', query)
	return HttpResponse(data, content_type='application/json')

def recipes(request):
	return db_to_json(models.Recipe.objects.all())

def ingredients(request):
	return db_to_json(models.Ingredient.objects.all())

def quantity_unit(request):
	return db_to_json(models.QuantityUnit.objects.all().order_by('num_order'))

def currency_unit(request):
	return db_to_json(models.CurrencyUnit.objects.all().order_by('num_order'))