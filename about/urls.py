from django.conf.urls import url,  include

from . import views
urlpatterns = [
    url(r'^$', views.about, name='About'),    
    url(r'^my-person$', views.about_my_person, name='About'),
    url(r'^my-tools$', views.about_my_tools, name='About'),
    url(r'^my-workspaces$', views.about_my_workspaces, name='About'),
    url(r'^my-toys$', views.about_my_toys, name='About'),
    url(r'^my-adventures$', views.about_my_adventures, name='About'),
]