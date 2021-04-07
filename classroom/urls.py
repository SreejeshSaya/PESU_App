from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('notifications', views.notificationsView, name='notifications')
]

# admin.site.site_url= None
# admin.site.site_header = 'My Site'