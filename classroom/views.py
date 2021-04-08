from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Student, Attendance, Teacher, Course, CourseEnrolled, Notification
from .forms import NotificationForm

@login_required
def indexView(request):
	print(f"indexView --- User: {request.user}")
	reqUser = request.user
	print(reqUser)
	if reqUser.is_authenticated:
		if reqUser.isTeacher:
			user = Teacher.objects.get(regNo=reqUser)
		else:
			user = Student.objects.get(srn=reqUser)
		return render(request, 'index.html', context={'user': user})
	# else:
	# 	return render(request, 'info/homepage.html')
	# return render(request, 'info/logout.html')

@login_required
def notificationsView(request):
	print(f"notificationsView --- {request.user}")
	notifs = Notification.objects.all()[:10]
	# print(notifs[0].name)
	# for notif in notifs:
	# 	notif['teacher'] = Teacher.objects.get(regNo=tRegNo)
	return render(request, 'notifications.html', context={'notifications': notifs})

@login_required
def createNotificationView(request):
	reqUser = request.user
	if reqUser.isTeacher:
		if request.method == 'POST':
			form = NotificationForm(request.POST)
			if form.is_valid():
				notif = form.save(commit=False)
				notif.teacher = Teacher.objects.get(regNo=reqUser.username)
				notif.save()
				return redirect('/notifications')
		else:
			form = NotificationForm()
			return render(request, 'create-notification.html', context={'form': form})