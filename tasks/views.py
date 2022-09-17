from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Create your views here.

def home(request):
	form = TaskForm(request.POST or None)
	tasks = Task.objects.all()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			t = request.POST.get('title')
			print(t)
			messages.info(request, 'You just added a new task!' +'('  + t + ')')
			return redirect('home')
	context = {'tasks':tasks, 'form':form}
	return render(request, 'index.html', context)