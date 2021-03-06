from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.indexView, name='index'),
    path('enter-attendance/', views.takeAttendance, name='enter-attendance'),
    path('view-attendance/', views.viewAttendance, name='view-attendance'),
    path('notifications/', views.notificationsView, name='notifications'),
    path('create-notification/', views.createNotificationView, name='create-notification'),
    path('student-feedback/', views.studentFeedback, name='student-feedback')
]