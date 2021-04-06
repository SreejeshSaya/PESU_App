from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student, Attendance, Teacher, Course, CourseEnrolled
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def indexView(request):
	print("Teacher?:", request.user.isTeacher)
	# if request.user.isTeacher:
	# 	return render(request, 'info/t_homepage.html')
	# else:
	# 	return render(request, 'info/homepage.html')
	# return render(request, 'info/logout.html')