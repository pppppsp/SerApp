from django.contrib import admin
from core.models import *

@admin.register(Journal)
class JournalModelAdmin(admin.ModelAdmin):
    list_display=['issn','language', 'levels']

@admin.register(Levels)
class LevelsModelAdmin(admin.ModelAdmin):
    list_display=['number']

@admin.register(Language)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(OpenAccess)
class OpenAccessModelAdmin(admin.ModelAdmin):
    list_display=['name',]

@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display=['name',]






