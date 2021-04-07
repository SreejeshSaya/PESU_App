from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
]

# admin.site.site_url= None
# admin.site.site_header = 'My Site'