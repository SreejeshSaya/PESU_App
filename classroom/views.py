from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student, Attendance, Teacher, Course, CourseEnrolled
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def indexView(request):
	print("Teacher?:", request.user.isTeacher)
	if request.user.isTeacher:
		return render(request, 't_homepage.html')
	# if request.user.isTeacher:
	# 	return render(request, 'info/t_homepage.html')
	# else:
	# 	return render(request, 'info/homepage.html')
	# return render(request, 'info/logout.html')

####Attendance####

@login_required

def t_clas(request, teacher_id, choice):
    teacher1 = get_object_or_404(Teacher, regNo=teacher_id)
    print(teacher1.course)
    choice = 1
    return render(request, 't_clas.html', {'teacher1': teacher1, 'choice': choice})

@login_required
def take_attendance(request, teacher_id, choice):
	teacher1 = get_object_or_404(Teacher, regNo=teacher_id)
	students1 = CourseEnrolled.objects.filter(courseCode=teacher1.course)
	return render(request, 'take_attendance.html', context = {"students1":students1})

@login_required
def att_confirm(request, teacher_id, choice):
	print(request)

# def viewAttendance(request):

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
			# for student in studentsPresent:
			# 	studentSRN = Student.objects.get(srn=student)
			# 	present = Attendance.objects.create(studentSRN=studentSRN, courseCode=course)
		elif request.method == 'GET':
			teacher = Teacher.objects.get(regNo=reqUser.username)
			studentList = CourseEnrolled.objects.filter(courseCode=teacher.course).values_list('studentSRN', flat=True).order_by('studentSRN')
			print(list(studentList))
			return render(request, 'take-attendance.html', context={'studentList': studentList})
