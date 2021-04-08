from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
	class Meta:
		model = Notification
		fields = ('title', 'description')
		widgets = {
			'title': forms.TextInput(),
			'description': forms.Textarea()
		}