from django.db import models
from django.core.validators import \
	MinValueValidator,\
	MaxValueValidator,\
	MinLengthValidator
	
from django.contrib.auth.models import AbstractUser

from choices import branchChoices

class MyUser(AbstractUser):
	@property
	def isTeacher(self):
		if hasattr(self, 'teacher'):
			return True
		return False

class Course(models.Model):
	code = models.CharField(max_length=13, primary_key=True, default="000000")
	name = models.CharField(max_length=30)
	branch = models.CharField(max_length=3, choices=branchChoices, default='CSE')
	credits = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])

class Student(models.Model):
	user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
	srn = models.CharField(max_length=13, primary_key=True, verbose_name="SRN", default="PES1201800000")
	name = models.CharField(max_length=20)
	email = models.EmailField(default="email@gmail.com")
	phNo = models.CharField(max_length=10, default="0000000000",validators=[MinLengthValidator(10)], verbose_name="Phone No.")
	dob = models.DateField(default='2000-05-05')
	age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18)])
	genderChoices = [ ('M', 'Male'), ('F', 'Female') , ('O', 'Other') ]
	gender = models.CharField(max_length=7, choices=genderChoices, default='Male')
	semester = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])
	cgpa = models.DecimalField(max_digits=4, default = 9, decimal_places=2, validators=[MinValueValidator(5.0), MaxValueValidator(10.0)])
	branch = models.CharField(max_length=3, choices=branchChoices, default='CSE')

	class Meta:
		ordering = ['srn']

	def get_absolute_url(self):
		return reverse('student', args=[self.srn])

	def __str__(self):
		return self.srn

class Teacher(models.Model):
	user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
	regNo = models.CharField(max_length=10, default="PESTECH000", primary_key=True, verbose_name="Reg No")
	name = models.CharField(max_length=20)
	email = models.EmailField(default="teacher@gmail.com")
	phNo = models.CharField(max_length=10, default="0000000000", validators=[MinLengthValidator(10)], verbose_name="Phone No.")
	genderChoices = [ ('M', 'Male'), ('F', 'Female') , ('O', 'Other') ]
	gender = models.CharField(max_length=7, choices=genderChoices, default='Male')

	department = models.CharField(max_length=3, choices=branchChoices, default='CSE')
	course = models.ForeignKey(Course, on_delete=models.PROTECT)

	def get_absolute_url(self):
		return reverse('teacher', args=[self.regNo])

	def __str__(self):
		return self.regNo

class CourseEnrolled(models.Model):
	studentSRN = models.ForeignKey(Student, on_delete=models.CASCADE)
	courseCode = models.ForeignKey(Course, on_delete=models.CASCADE)
	# semester = StudentSRN.semester
	class Meta():
		verbose_name = "Courses Enrolled"

class Attendance(models.Model):
	studentSRN = models.ForeignKey(Student, on_delete=models.CASCADE)
	courseCode = models.ForeignKey(Course, on_delete=models.CASCADE)
	classDate = models.DateField()
	attended = models.BooleanField(default='False')

	class Meta():
		verbose_name = "Student Attendance"

	def __str__(self):
		sname = Student.objects.get(name=self.student)
		cname = Course.objects.get(name=self.course)
		return '%s : %s' % (sname.name, cname.id)