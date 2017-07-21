# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import GalleryImage

def gallery_items(request):
	
	queryset = GalleryImage.objects.all()
	context = {
		"object_list": queryset
	}

	return render(request, 'gallery/gallery.html', context)