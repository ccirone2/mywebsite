# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class GalleryImage(models.Model):
	
	image 					= models.ImageField(blank=False, upload_to='gallery/static/gallery/img')

	image_title 			= models.CharField(max_length=120)
	image_subtitle 			= models.CharField(max_length=120, null=True, blank=True)
	image_description 		= models.TextField(null=True, blank=True)
	
	date_built				= models.DateTimeField(auto_now=False, auto_now_add=False)
	date_uploaded			= models.DateTimeField(auto_now_add=True)
	date_updated			= models.DateTimeField(auto_now=True)

	def __str__(self):
	 	return self.image_title