from django import forms
from pagedown.widgets import PagedownWidget
from .models import *

class Article(forms.ModelForm):
    title = forms.CharField()
    lead = forms.CharField()

    text = forms.CharField(widget=PagedownWidget(show_preview=False))


    class Meta:
        model = Article
        fields = ["title","lead" ,"text", "tags"]
#class Teacher(forms.ModelForm)