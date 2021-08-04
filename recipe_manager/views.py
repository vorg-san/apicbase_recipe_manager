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
		form = forms.IngredientForm(request.POST, request.FILES)

		if form.is_valid():
			if form.cleaned_data['image']:
				ingredient.image = models.Ingredient(image=form.cleaned_data['image']).image
			if form.cleaned_data['remove_image']:
				ingredient.image = None
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

def get_recipe_and_price_lists(recipe_id):
	recipe_list = models.RecipeList.objects.filter(recipe=recipe_id)
	price_list = {}
	
	for ingredient_list in recipe_list.all():
		price_list[ingredient_list.ingredient.id] = ingredient_list.quantity * ingredient_list.ingredient.currency / ingredient_list.ingredient.quantity

	return [recipe_list, price_list]

def add_recipe_ingredient(request):
	if request.method == 'POST':
		form_ingredient = forms.RecipeIngredientForm(request.POST)

		if form_ingredient.is_valid():
			recipe_id = request.POST.get('recipe_id', '')
			ingredient_id = request.POST.get('ingredient_id', '')
			quantity = form_ingredient.cleaned_data['quantity']
			recipe_list, _ = get_recipe_and_price_lists(recipe_id)
			
			if not recipe_list.filter(ingredient=ingredient_id): # can't add if ingredient is already in the recipe
				recipe_list_new = models.RecipeList()
				recipe_list_new.recipe = get_object_or_404(models.Recipe, pk=recipe_id)
				recipe_list_new.quantity = quantity 
				recipe_list_new.ingredient = get_object_or_404(models.Ingredient, pk=ingredient_id)
				recipe_list_new.save()
				
		return HttpResponseRedirect(reverse(f'recipe_manager:edit recipe', kwargs={'recipe_id':recipe_id}))

def edit_recipe(request, recipe_id):
	recipe = models.Recipe()
	recipe_list = []
	initial_name_form = {}
	price_list = {}
	form_ingredient = forms.RecipeIngredientForm(initial={'recipe_id': recipe.id})

	if recipe_id > 0:
		recipe = get_object_or_404(models.Recipe, pk=recipe_id)
		initial_name_form = {
			'name': recipe.name,
		}
		recipe_list, price_list = get_recipe_and_price_lists(recipe_id)
		
	ingredients_in_recipe = [rl.ingredient.id for rl in recipe_list]
				
	if request.method == 'POST':
		form_name = forms.RecipeNameForm(request.POST)

		if form_name.is_valid():
			recipe.name = form_name.cleaned_data['name']
			recipe.save()			
			
			return HttpResponseRedirect(reverse(f'recipe_manager:edit recipe', kwargs={'recipe_id':recipe.id}))
	else:
		form_name = forms.RecipeNameForm(initial=initial_name_form)
	
	context = {
		'form_name': form_name,
		'form_ingredient': form_ingredient,
		'recipe': recipe,
		'recipe_list': recipe_list,
		'price_list': price_list,
		'ingredients_in_recipe': ingredients_in_recipe,
		'ingredients': models.Ingredient.objects.all(),
	}

	return render(request, 'recipe_manager/edit_recipe.html', context)


# Remove endpoints
def remove_ingredient(request, ingredient_id):
	ingredient = get_object_or_404(models.Ingredient, pk=ingredient_id)
	ingredient.delete()
	return HttpResponseRedirect(reverse('recipe_manager:home') )

def remove_recipe(request, recipe_id):
	recipe = get_object_or_404(models.Recipe, pk=recipe_id)
	recipe.delete()
	return HttpResponseRedirect(reverse('recipe_manager:home'))

def remove_recipe_ingredient(request, recipe_id, ingredient_id):
	models.RecipeList.objects.filter(recipe=recipe_id, ingredient=ingredient_id).delete()
	return HttpResponseRedirect(reverse('recipe_manager:edit recipe', kwargs={'recipe_id':recipe_id}))
# Remove endpoints


# Filters
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter
def sum_dict_items(dictionary):
	return sum([dictionary.get(key) for key, _ in dictionary.items()])

@register.filter
def contains(list, element):
	if not list:
		return False
	return element in list
# Filters



# Below would be used only for integration with a pure js framework like React
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