from django.contrib import admin

from .models import Formulario, Projetos, ProjetosTags

# Register your models here.
admin.site.register(Formulario)
admin.site.register(Projetos)
admin.site.register(ProjetosTags)

