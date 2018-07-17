from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import Teacher, School

def login(request):
    return render(request,'login.html')


@login_required
def index(request):
    tekst = 'hello misiu'
    return render(request, 'index.html', {'tekst':tekst})