# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def about(request):
	return render(request, 'about/about.html')

def about_my_person(request):
	return render(request, 'about/about.html')

def about_my_tools(request):
	return render(request, 'about/about.html')

def about_my_workspaces(request):
	return render(request, 'about/about.html')

def about_my_toys(request):
	return render(request, 'about/about.html')

def about_my_adventures(request):
	return render(request, 'about/about.html')
