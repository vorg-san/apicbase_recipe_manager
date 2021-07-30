from django import forms

class IngredientForm(forms.Form):
	name = forms.CharField(max_length=300)
	quantity = forms.FloatField()
	# quantityUnit = forms.ForeignKey(QuantityUnit, on_delete=models.CASCADE)
	currency = forms.FloatField()
	# currencyUnit = forms.ForeignKey(CurrencyUnit, on_delete=models.CASCADE)
