from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs = {'placeholder': 'Add New Task', 'bg-primary'
  'border':  '30px solid red' }))
	class Meta:
		model = Task
		fields = ['title']
