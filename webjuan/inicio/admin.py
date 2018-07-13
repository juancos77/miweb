# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bienvenido

@admin.register(Bienvenido)
class BienvenidoAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname',)
