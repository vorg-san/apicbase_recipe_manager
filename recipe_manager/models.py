from django.db import models
from django.utils import timezone

class QuantityUnit(models.Model):
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.description

class CurrencyUnit(models.Model):
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.description

class Ingredient(models.Model):
	name = models.CharField(max_length=300)
	quantity = models.FloatField()
	quantityUnit = models.ForeignKey(QuantityUnit, on_delete=models.CASCADE)
	currency = models.FloatField()
	currencyUnit = models.ForeignKey(CurrencyUnit, on_delete=models.CASCADE)
	updated = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=800)
	updated = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.name

class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	ammount = models.FloatField()