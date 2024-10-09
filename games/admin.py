from django.contrib import admin
from . models import *

class JogoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao', 'data_modificacao']
    search_fields = ['nome']

admin.site.register(Jogo, JogoAdmin)