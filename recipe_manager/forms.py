from django import forms
from . import models

class IngredientForm(forms.Form):
	name = forms.CharField(max_length=300)
	article = forms.CharField(max_length=300)
	quantity = forms.FloatField()
	quantityUnit = forms.ModelChoiceField(queryset=models.QuantityUnit.objects.all().order_by('num_order'))
	currency = forms.FloatField()
	currencyUnit = forms.ModelChoiceField(queryset=models.CurrencyUnit.objects.all().order_by('num_order'))
	image = forms.ImageField(required=False)
	remove_image = forms.BooleanField(required=False,label='Remove image')

class RecipeNameForm(forms.Form):
	name = forms.CharField(max_length=800)

class RecipeIngredientForm(forms.Form):
	quantity = forms.FloatField() 
	recipe_id = forms.HiddenInput()
	ingredient_id = forms.HiddenInput()
        