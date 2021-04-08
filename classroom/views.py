from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Student, Attendance, Teacher, Course, CourseEnrolled, Notification, Feedback
from .forms import NotificationForm, FeedbackForm

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

@login_required
def notificationsView(request):
	print(f"notificationsView --- {request.user}")
	notifs = Notification.objects.all()[:10]
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

@login_required
def studentFeedback(request):
	reqUser = request.user
	if not reqUser.isTeacher:
		print("User is not Teacher")
		if request.method == 'POST':
			feedback = Feedback.objects.filter(studentSRN=reqUser.username, courseCode=request.POST['courseCode'])
			if feedback.exists():
				return render(request, 'student-feedback.html', context={'feedbackSubmitted': True})
			form = FeedbackForm(request.POST)
			print("FORM VALID")
			feedback = form.save(commit=False)
			feedback.studentSRN = Student.objects.get(srn=reqUser.username)
			feedback.courseCode = Course.objects.get(code=request.POST['courseCode'])
			print(feedback)
			feedback.save()
			return redirect('/')
		else:
			form = FeedbackForm(reqUser.username)
			return render(request, 'student-feedback.html', context={'form': form, 'feedbackSubmitted': False})

@login_required
def viewAttendance(request):
	reqUser = request.user
	if not reqUser.isTeacher:
		attendance = Attendance.objects.filter(studentSRN=reqUser.username)
		return render(request, 'view-attendance.html', context={'attendance': attendance})

@login_required
def takeAttendance(request):
	reqUser = request.user
	print(reqUser.isTeacher)
	if reqUser.isTeacher:
		course = Teacher.objects.get(regNo=reqUser.username).course
		print(course.code)
		if request.method == 'POST':
			studentsPresent = list(request.POST.dict().keys())
			studentsPresent.remove('csrfmiddlewaretoken')
			print(studentsPresent)
			studentsEnrolled = CourseEnrolled.objects.filter(courseCode=course).select_related('studentSRN')
			print(studentsEnrolled)
			for student in studentsEnrolled:
				attended = False
				if student.studentSRN.srn in studentsPresent:
					attended = True
				dailyAtt = Attendance.objects.create(studentSRN=student.studentSRN, courseCode=course, attended=attended)
				dailyAtt.save()
			return redirect('/')

		elif request.method == 'GET':
			teacher = Teacher.objects.get(regNo=reqUser.username)
			studentList = CourseEnrolled.objects.filter(courseCode=teacher.course).values_list('studentSRN', flat=True).order_by('studentSRN')
			print(list(studentList))
			return render(request, 'take-attendance.html', context={'studentList': studentList})