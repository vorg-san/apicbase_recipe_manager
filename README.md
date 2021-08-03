# apicbase_recipe_manager

1 week coding challenge from Apicbase, it is my first django app. The requirements were:

Description

Create a small Recipe Manager application in Django (Python) in which you can create ingredients and recipes and that allows the calculation of food cost for the recipes.

Technical Requirements

A. Ingredients
	1. An ingredient minimally has a name, an article number and a cost for a certain amount. Example: The ingredient “carrot” has a cost of 1 EURO per 500 grams.
	2. You need to minimally support the following units: ‘grams’, ‘kilograms’, ‘centiliter’, ‘liter’.
	3. There should be a page to add a new ingredient
	4. There should be a page to edit an existing ingredient.
	5. There should be a page to view all ingredients.
	6. A user should be able to search his ingredients based on name or article number.
B. Recipes
	1. A recipe minimally has a name and a list of ingredients with the amounts needed. Example the Recipe for “Carrot Cake” contains 100 grams of “carrot” and 50 centiliters of “cream”.
	2. There should be a page to create new recipes.
	3. There should be a page to edit existing recipes.
	4. There should be a page to view all recipes.
	5. There should be a page to see the details of a recipe. This page should show the name but also the cost for each ingredient used in the recipe (example: the 100 grams of “carrot” in the “Carrot Cake” recipe would cost 0.2 EURO) and then the total cost for the recipe.

## Setup

1) Create Mysql instance
2) Set enviroment variables:
	- 'DJANGO_RECIPE_MANAGER_SECRET_KEY' - random secret string 
	- 'MYSQL_USER' - mysql database user
	- 'MYSQL_PASS' - mysql database password
	- 'MYSQL_HOST' - mysql database url
3) Clone repo
4) cd into cloned repo folder
5) run: python manage.py runserver