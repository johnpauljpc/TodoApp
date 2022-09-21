from django.shortcuts import render, redirect, get_object_or_404
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

def update(request, pk):
	obj = get_object_or_404(Task, id=pk)

	form  = TaskForm(request.POST or None, instance = obj)
	get_updated_task = request.POST.get('title')
	
	get_task_title = obj.title
	if request.method == 'POST':
		if form.is_valid():
			t1 = request.POST.get('task')
			print('t1', t1)
			form.save()
			t = request.POST.get('task')
			print('t', t)
			messages.info(request, 'You updated task' +'('  + get_task_title + '' + ') to '+ get_updated_task )
			return redirect('/')

	context = {'form':form, 'obj':obj}

	return render(request, 'update.html', context)


def delete(request, pk):
	#obj = Task.objects.get(id = pk)
	obj = get_object_or_404(Task, id = pk)
	obj_task = obj.title

	if request.method == 'POST':
		obj.delete()
		#obj_task = obj_task.title
		messages.info(request, 'You have deleted a task' +'('  +  obj_task + ')!')
		return redirect('/')
	

	return render(request, 'delete.html', {'obj':obj})


def complete(request, pk):
	obj = Task.objects.get(id = pk)
	option = obj.complete
	print("This is option  ", obj)
	ts = str(obj)
	if option == True:
		obj.complete = False
		
		obj.save()
		messages.info(request, "Task (" + ts + ") Not done")
		return redirect('/')
	else:
		obj.complete = True
		obj.save()
		messages.success(request, "Completed task")
		return redirect('/')

	return render(request, 'index.html')