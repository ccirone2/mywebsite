# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def projects(request):
	return render(request, 'projects/projects.html')

def projects_in_review(request):
	return render(request, 'projects/projects.html')

def projects_in_concept(request):
	return render(request, 'projects/projects.html')

def projects_in_progress(request):
	return render(request, 'projects/projects.html')