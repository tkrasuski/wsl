from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Teacher, School, Article

def login(request):
    return render(request,'login.html')


@login_required
def index(request):
    tekst = 'hello misiu'
    return render(request, 'index.html', {'tekst':tekst})

def article(request,id):
    try:
        art = Article.objects.get(id=id)
        return render(request,'article.html',{'art':art})
    except:
        msg = "<B>No such thing</B>"
        return HttpResponse(msg)