from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    if request.user.is_authenticated:
        context = {
        'todos' : todos
        }
        return render(request, 'todos/index.html', context)
    else:
        return redirect('accounts:login')



def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('todos:index')
        else:
            form = TodoForm()
        context = {
            'form': form,
        }
        return render(request, 'todos/create.html', context)
    else:
        return redirect('accounts:login')