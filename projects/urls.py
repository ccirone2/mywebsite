from django.conf.urls import url,  include

from . import views
urlpatterns = [
    url(r'^$', views.projects, name='Projects'),    
    url(r'^in-concept$', views.projects_in_concept, name='Projects in Concept'),
    url(r'^in-review$', views.projects_in_review, name='Projects in Review'),
    url(r'^in-progress$', views.projects_in_progress, name='Projects in Progress'),
]