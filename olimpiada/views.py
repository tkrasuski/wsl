from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Teacher, School, Article
from .forms import *

def userlogin(request):
    #print (request.user.login)
    arts = Article.objects.filter(position__startswith='login')
    message = None
    if request.method=='POST':
        data = request.POST
        #print (data) 
        user_ = data['username']
        pass_ = data['password']
        user = authenticate(username=user_, password=pass_)
       #print (user)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            message = 'Nieprawidłowa nazwa użytkownika lub hasło'
            return render(request, 'login.html', {'arts':arts, 'message':message})
    else:
        return render(request, 'login.html', {'arts':arts, 'message':message})
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
@login_required
def index(request):
    try:
        arts = Article.objects.filter(position__startswith='index')
        #arts = Article.objects.all()
       # print (list(arts))
        return render(request, 'index.html', {'arts':arts})
    except:
        msg = "<B>Error</B>"
        raise
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

@login_required
def students(request):
    user = Teacher.objects.get(user=request.user)
    myschoolid = user.school.id
    students = Student.objects.filter(school=myschoolid)
    if not students:
        students=None
    return render(request, 'students.html',{'students':students})

@login_required
def student(request,id):
    user = Teacher.objects.get(user=request.user)
    myschoolid = user.school.id
    st = Student.objects.get(id=id)
    initials = dict(first_name=st.first_name, last_name=st.last_name, classe=st.classe)
    form = StudentForm(initial=initials)
    if request.method=='POST':
        pass
    
    return render(request, 'student.html',{'form':form})
def registerschool(request):
    form = SchoolForm()
    if request.method=='POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            school = School()
            school.school = data['school']
            school.street = data['street']
            school.zip_code = data['zip_code']
            school.city = data['city']
            school.voivodeship = data['voivodeship']
            school.authority = data['authority']
            school.phone_number = data['phone_number']
            school.principal_name = data['principal_name']
            school.save()
            obj = School.objects.latest('id')
            request.session['myschool'] = obj.id
            return HttpResponseRedirect('/registeruser')

    return render(request, 'school.html',{'form':form})
def registeruser(request):
    form = RegisterUserForm()
    if request.method =='POST':
        form = form = RegisterUserForm(request.POST)
        if form.is_valid():
            myschool = School.objects.get(id=int(request.session['myschool']))
            print (myschool)
            data = form.cleaned_data
            teacher = Teacher()
            teacher.first_name = data['first_name']
            teacher.last_name = data['last_name']
            teacher.position = data['position']
            teacher.phone_no = data['phone_number']
            teacher.email = data['email']
            teacher.school = myschool
            # creating user account
            user = User.objects.create_user(username=data['login'], email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'], is_active=False)
            teacher.user = user
            teacher.save()
            return HttpResponseRedirect('/registerinfo')
    return render(request, 'registeruser.html',{'form':form})
def registerinfo(request):
    arts = Article.objects.filter(position__startswith='registerinfo')
    return render(request, 'registerinfo.html',{'arts':arts})
def registration(request):
    arts = Article.objects.filter(position__startswith='registration')
    return render(request, 'registration.html',{'arts':arts})