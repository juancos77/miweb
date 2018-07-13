# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bienvenido

def bienvenido(request):
    bienvenidos.Bienvenido.objects.order_by('id')
    template = loader.get_template('bienvenido.html')
    title = 'Bienvenido a mi web'
    context = {
        'bienvenidos': bienvenidos,
        'title': title
    }
    return HttpResponse(template.render(context, request))
