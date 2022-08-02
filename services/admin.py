from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


# admin.site.register(models.EquipmentPrice)


class SchemeItemInline(admin.TabularInline):
    model = models.SchemeItem
    extra = 0


class ProjectPropertyInline(admin.TabularInline):
    model = models.ProjectProperty
    extra = 0


class ProjectImagesInline(admin.TabularInline):
    model = models.ProjectImage
    extra = 0
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="150" style="border: 1px solid #ddd;">')

    get_image.short_description = ''


class EquipmentPropertyInline(admin.TabularInline):
    model = models.EquipmentProperty
    extra = 0


class TypeInline(admin.TabularInline):
    model = models.Type
    extra = 0


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_full', 'slug',)
    inlines = (TypeInline,)
    prepopulated_fields = {'slug': ('title',), }
    save_as = True
    save_on_top = True
    ordering = ('id',)
    readonly_fields = ('get_image_preview', 'get_image_detail')
    fieldsets = (
        ('Основное', {'fields': (('title', 'title_full', 'slug'),)}),
        (None, {'fields': ('description', 'description_full')}),
        ('Картинки', {'fields': (
            ('image_preview', 'get_image_preview'), ('image_detail', 'get_image_detail'))}),
        ('Проекты', {'fields': ('projects_header', 'projects_text', 'projects')}),
        ('Техника', {'fields': ('equipment_header',
         'equipment_text', 'equipment')}),
        ('Дополнительные услуги', {'fields': ('types_header', 'types_text')}),
    )

    def get_image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image_preview.url}" width="150" style="max-width:100%;border: 1px solid #ddd;">')

    def get_image_detail(self, obj):
        return mark_safe(f'<img src="{obj.image_detail.url}" width="150" style="max-width:100%;border: 1px solid #ddd;">')

    get_image_preview.short_description, get_image_detail.short_description = 'Превью', 'Детальная картинка'


@admin.register(models.Project)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = (ProjectImagesInline, ProjectPropertyInline,)
    save_as = True
    save_on_top = True
    ordering = ('id',)


# @admin.register(models.ProjectPropertyName)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     save_as = True
#     save_on_top = True
#     ordering = ('title',)


@admin.register(models.Equipment)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'price', 'price_type',)
    readonly_fields = ('get_image_big',)
    inlines = (EquipmentPropertyInline,)
    save_as = True
    save_on_top = True
    ordering = ('id',)
    list_editable = ('price', 'price_type',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" style="border: 1px solid #ddd;">')

    def get_image_big(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:300px;max-width:100%;border: 1px solid #ddd;">')

    get_image.short_description, get_image_big.short_description = 'Картинка', 'Картинка'


# @admin.register(models.EquipmentPropertyName)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('title',)
#     save_as = True
#     save_on_top = True
#     ordering = ('title',)


@admin.register(models.Scheme)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('scheme',)
    inlines = (SchemeItemInline,)
    save_as = True
    save_on_top = True
    ordering = ('id',)


@admin.register(models.Document)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image',)
    readonly_fields = ('get_image_big',)
    save_as = True
    save_on_top = True
    ordering = ('id',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" style="border: 1px solid #ddd;">')

    def get_image_big(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:300px;max-width:100%;border: 1px solid #ddd;">')

    get_image.short_description, get_image_big.short_description = 'Картинка', 'Картинка'


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
