# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False,)
    apellidoP = models.CharField(max_length = 50, null = False, blank = False,)
    apellidoM = models.CharField(max_length = 50, null = True, blank = True,)
    edad = models.PositiveSmallIntegerField(null = False, blank = False,)
    curp = models.CharField(max_length = 18, null = True, blank = True,)
    domicilio = models.CharField(max_length = 100, null = True, blank = True,)
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_CHOICES = ((MASCULINO, 'Masculino'), (FEMENINO, 'Femenino'))
    sexo = models.CharField(max_length = 1, choices = SEXO_CHOICES, default = MASCULINO)
