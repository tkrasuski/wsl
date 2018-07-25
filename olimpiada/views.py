from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Teacher, School, Article
from .forms import *
def login(request):
    return render(request,'login.html')

def login(request):
    arts={}
    return render(request, 'login.html', {'arts':arts})

@login_required
def index(request):
    try:
        arts = Article.objects.filter(position__startswith='index')
        #arts = Article.objects.all()
       # print (list(arts))
        return render(request, 'index.html', {'arts':arts})
    except:
        msg = "<B>Error</B>"
       # raise
        return HttpResponse(msg)
@login_required
def article(request,id):
    try:
        art = Article.objects.get(id=id)
        return render(request,'article.html',{'art':art})
    except:
        msg = "<B>No such thing</B>"
        return HttpResponse(msg)

# Widok edycji profilu nauczyciela
@login_required
def profile(request):
    user = Teacher.objects.get(user=request.user)
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.position = data['position']
            user.email = data['email']
            user.phone_no = data['phone_number']
            user.save()
            return HttpResponseRedirect('/')

    else:
        initial = dict(first_name=user.first_name, last_name=user.last_name, position=user.position, email=user.email, phone_number=user.phone_no)
        form = ProfileForm(initial=initial)
        
    return render(request, 'profile.html',{'form':form})


# widok do edycji danych szkoły
@login_required
def school(request):
    user = Teacher.objects.get(user=request.user)
    myschoolid = user.school.id
    myschool = School.objects.get(id=myschoolid)
    if request.method=='POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            myschool.school = data['school']
            myschool.street = data['street']
            return HttpResponseRedirect('/')
    else:
        initial = dict(school=myschool.school, street=myschool.street, zip_code=myschool.zip_code, city=myschool.city, voivodeship=myschool.voivodeship, authority=myschool.authority, phone_number=myschool.phone_number, email=myschool.email, principal_name=myschool.principal_name)
        form = SchoolForm(initial=initial)
    return render(request, 'school.html',{'form':form})


