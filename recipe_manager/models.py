from django.db import models
from django.utils import timezone

class QuantityUnit(models.Model):
	description = models.CharField(max_length=100)
	num_order = models.IntegerField()

	def __str__(self):
		return self.description

class CurrencyUnit(models.Model):
	description = models.CharField(max_length=100)
	num_order = models.IntegerField()

	def __str__(self):
		return self.description

class Ingredient(models.Model):
	name = models.CharField(max_length=300)
	article = models.CharField(max_length=300)
	quantity = models.FloatField()
	quantityUnit = models.ForeignKey(QuantityUnit, on_delete=models.CASCADE)
	currency = models.FloatField()
	currencyUnit = models.ForeignKey(CurrencyUnit, on_delete=models.CASCADE)
	updated = models.DateTimeField(default=timezone.now, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=800)
	ingredients = models.ManyToManyField(Ingredient, through='RecipeList')
	updated = models.DateTimeField(default=timezone.now, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class RecipeList(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.FloatField()