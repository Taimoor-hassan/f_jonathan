from django.contrib import admin
from .models import card

class filter(admin.ModelAdmin):
    list_display=('name','choseprogress',)
    search_fields=('name','choseprogress',)
    list_filter=('name','choseprogress',)


# Register your models here.
admin.site.register(card,filter)