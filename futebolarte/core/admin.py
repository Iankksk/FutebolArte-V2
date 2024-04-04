from django.contrib import admin
from .models import Clube


@admin.register(Clube)
class AdminClube(admin.ModelAdmin):
    list_display = ['nome', 'cidade', 'cores', 'ano_fundacao', 'tem_mundial']


