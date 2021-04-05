from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Student, Teacher

admin.site.register(MyUser, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
