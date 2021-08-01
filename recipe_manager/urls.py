from django.urls import path

from . import views

app_name = "recipe_manager"
urlpatterns = [
	path("", views.home, name="home"),
	path("ingredient/<int:ingredient_id>/", views.edit_ingredient, name="edit ingredient"),
	path("recipe/<int:recipe_id>/", views.edit_recipe, name="edit recipe"),

	path("recipe/", views.recipes, name="recipes"),
	path("ingredient/", views.ingredients, name="ingredients"),
	path("quantity_unit/", views.quantity_unit, name="quantity unit"),
	path("currency_unit/", views.currency_unit, name="currency unit"),
]
