from django.shortcuts import get_object_or_404, render
from datetime import date
from datetime import timedelta as td
from .models import Task, Project

def index(request):
    latest_task_list = Task.objects.filter(start__gte=date.today()-td(days=5))
    context = {'latest_task_list': latest_task_list}
    return render(request, 'toggls/index.html', context)

