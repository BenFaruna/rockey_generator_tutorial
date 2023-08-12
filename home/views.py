# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {'heading': 'Tutorial Dashboard'}
    # Page from the theme 
    return render(request, 'pages/index.html', context=data)

def authors(request):
    return render(request, 'pages/authors.html')