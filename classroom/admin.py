from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser,\
					Student,\
					Teacher,\
					Course,\
					CourseEnrolled,\
					Attendance,\
					Notification

admin.site.register(MyUser, UserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(CourseEnrolled)
admin.site.register(Attendance)
admin.site.register(Notification)
