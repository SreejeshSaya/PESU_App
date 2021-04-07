from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<int:assign_id>/Extra_class/', views.t_extra_class, name='t_extra_class'),
]

# admin.site.site_url= None
# admin.site.site_header = 'My Site'