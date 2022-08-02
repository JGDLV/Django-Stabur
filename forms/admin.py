from django.contrib import admin
from . import models


# @admin.register(models.TestFormModel)
# class TestFormModel(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'comment', 'create_at', )
#     readonly_fields = ('name', 'phone', 'comment', 'create_at', )


@admin.register(models.ContactForm)
class ContactForm(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment', 'create_at', )
    readonly_fields = ('name', 'phone', 'comment', 'create_at', )


@admin.register(models.CallbackForm)
class CallbackForm(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment', 'create_at', )
    readonly_fields = ('name', 'phone', 'comment', 'create_at', )


@admin.register(models.EquipmentForm)
class EquipmentForm(admin.ModelAdmin):
    list_display = ('equipment', 'name', 'phone', 'address',
                    'date', 'time', 'create_at', )
    readonly_fields = ('equipment', 'name', 'phone', 'address',
                       'date', 'time', 'comment', 'create_at', )


@admin.register(models.ServiceForm)
class ServiceForm(admin.ModelAdmin):
    list_display = ('service', 'name', 'phone', 'address', 'create_at', )
    readonly_fields = ('service', 'address', 'name',
                       'phone', 'comment', 'create_at', )
