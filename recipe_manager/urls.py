from django.urls import path

from . import views

app_name = "recipe_manager"
urlpatterns = [
	path("recipe/", views.recipes, name="recipes"),
	path("ingredient/", views.ingredients, name="ingredients"),
	path("quantity_unit/", views.quantity_unit, name="quantity unit"),
	path("currency_unit/", views.currency_unit, name="currency unit"),
	path("recipe/<int:recipe_id>/", views.recipe_details, name="recipe details"),
]
