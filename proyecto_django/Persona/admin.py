# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..Persona.models import Persona
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidoP', 'apellidoM', 'edad', 'curp',)
    list_filter = ('edad', 'sexo',)
