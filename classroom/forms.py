from django import forms
from .models import Notification, Feedback, CourseEnrolled, Course

class NotificationForm(forms.ModelForm):
	class Meta:
		model = Notification
		fields = ('title', 'description')
		# Akhil, for the form input tags, check out this website to see how to 
		# add classes and other attributes
		# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#overriding-the-default-fields
		# https://stackoverflow.com/questions/5827590/css-styling-in-django-forms
		widgets = {
			'title': forms.TextInput(),
			'description': forms.Textarea()
		}

class FeedbackForm(forms.ModelForm):
	feedChoices = [
		(1, 'Very Bad'),
		(2, 'Bad'),
		(3, 'Average'),
		(4, 'Good'),
		(5, 'Very Good')
	]

	def __init__(self, userSRN, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)

		coursesQuery = CourseEnrolled.objects.filter(studentSRN=userSRN).select_related('courseCode')
		course = []
		for c in coursesQuery:
			code = c.courseCode.code
			course.append((code, code))

		self.fields['courseCode'] = forms.ChoiceField(choices=course)
		self.fields['teaching'] = forms.ChoiceField(widget=forms.RadioSelect, choices=self.feedChoices)
		self.fields['syllabus'] = forms.ChoiceField(widget=forms.RadioSelect, choices=self.feedChoices)
		self.fields['doubtClar'] = forms.ChoiceField(widget=forms.RadioSelect, choices=self.feedChoices)

	class Meta:
		model = Feedback
		fields = ('courseCode', 'teaching', 'syllabus', 'doubtClar', 'miscFeedback')
		widgets = {
			'miscFeedback': forms.Textarea()
		}