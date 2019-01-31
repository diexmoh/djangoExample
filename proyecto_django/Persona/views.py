# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.list import ListView
from ..Persona.models import Persona

# Create your views here.

class ListViewPersona(ListView):
    model = Persona
    template_name = 'index.html'
    context_object_name = 'personas'
