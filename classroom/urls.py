from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('enter-attendance/', views.takeAttendance, name='enter-attendance')
]

# admin.site.site_url= None
# admin.site.site_header = 'My Site'