from django.contrib import admin

from .models import Category, Type, Manufacturer, Furniture


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type', 'name', 'image', 'manufacturer')
    list_display_links = ('pk', 'name')
    list_filter = ('type', 'manufacturer')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')
    list_display_links = ('pk', 'name')
    list_filter = ('category',)
    ordering = ('pk', )


admin.site.register(Category)
admin.site.register(Type, TypeAdmin)
admin.site.register(Manufacturer)
admin.site.register(Furniture, FurnitureAdmin)
