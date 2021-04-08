from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<slug:teacher_id>/<int:choice>/take-attendance', views.take_attendance, name='take_attendance'),
    path('teacher/<slug:teacher_id>/<int:choice>/att-confirm', views.att_confirm, name='att_confirm')
]

# admin.site.site_url= None
# admin.site.site_header = 'My Site'