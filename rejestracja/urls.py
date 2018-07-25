"""rejestracja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from  rejestracja import settings
from django.contrib import admin
from django.urls import path,  re_path
from olimpiada import views
from django.views.generic import FormView
from olimpiada import forms
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.index),
    path('index/', views.index),
    re_path(r'^form/$', FormView.as_view(template_name="form.html",form_class=forms.Article)),
    re_path(r'^article/(?P<id>\d+)/$', views.article),
    re_path(r'^profile/$', views.profile),
    re_path(r'^school/$', views.school),
    re_path(r'^students/$', views.students),
    re_path(r'^student/(?P<id>\d+)/$', views.student),
    re_path(r'^accounts/login/$', views.userlogin),
    re_path(r'^accounts/logout/$', views.userlogout),
    
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
