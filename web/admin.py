from django.contrib import admin
from .models import Contact,Update,Gallery


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name',)

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)
