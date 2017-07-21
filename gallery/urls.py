from django.conf.urls import url,  include
from django.views.generic import ListView, DetailView
#from blog.models import Post


from . import views
urlpatterns = [
    url(r'^$', views.gallery_items, name='Gallery'),    
]

#urlpatterns = [ 
#	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="gallery/gallery.html")),
#	url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post, template_name = 'gallery/post.html'))
#]