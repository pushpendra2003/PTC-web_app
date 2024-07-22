from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task, Click, Withdrawal
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Task.objects.all()
    return render(request, 'main/dashboard.html', {'tasks': tasks})

@login_required
def click_task(request, task_id):
    task = Task.objects.get(id=task_id)
    Click.objects.create(user=request.user, task=task)
    return redirect('dashboard')

@login_required
def withdrawal(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        Withdrawal.objects.create(user=request.user, amount=amount)
    return render(request, 'main/withdrawal.html')
