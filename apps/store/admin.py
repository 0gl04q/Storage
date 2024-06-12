from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from apps.store.models import manuals_models, movement_models


@admin.register(manuals_models.Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """ Админ-панель MPTT категорий """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(manuals_models.Units)
class UnitsAdmin(admin.ModelAdmin):
    """ Админ-панель единиц измерения """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(manuals_models.Brand)
class UnitsAdmin(admin.ModelAdmin):
    """ Админ-панель бренда """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(manuals_models.Counterparty)
class UnitsAdmin(admin.ModelAdmin):
    """ Админ-панель контрагентов """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(manuals_models.Delivery)
class UnitsAdmin(admin.ModelAdmin):
    """ Админ-панель доставки """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(manuals_models.Product)
class UnitsAdmin(admin.ModelAdmin):
    """ Админ-панель товаров """
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(movement_models.Movement)
admin.site.register(movement_models.StrProduct)
