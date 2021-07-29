from django.contrib import admin

from .models import QuantityUnit, CurrencyUnit, Ingredient

admin.site.register(QuantityUnit)
admin.site.register(CurrencyUnit)
admin.site.register(Ingredient)