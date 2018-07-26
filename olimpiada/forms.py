from django import forms
from pagedown.widgets import PagedownWidget
from .models import *

def validate_(value):
    if value in ('-','---'):
        raise forms.ValidationError('Proszę wybrać wartość z listy')
def validate_length(value):
    if len(value)<8:
        raise forms.ValidationError('Nazwa użytkownika musi mieć przynajmniej 8 znaków')
def validate_email(value):
    if not '@' in value:
        raise forms.ValidationError('Podaj prawidłowy adres email')
class Article_(forms.ModelForm):
    title = forms.CharField()
    lead = forms.CharField()
    text = forms.CharField(widget=PagedownWidget(show_preview=True))
    class Meta:
        model = Article
        fields = ["title","lead" ,"text", "tags"]
class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Imię',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Imię'}))
    last_name = forms.CharField(label='Nazwisko',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nazwisko'}))
    position = forms.CharField(label='Tytuł lub stopień zawodowy / naukowy',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Tytuł lub stopień zawodowy / naukowy'}))
    phone_number = forms.CharField(label='Numer telefonu',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Numer telefonu'}))
    email = forms.CharField(label='E-mail',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'E-mail'}))

class RegisterUserForm(forms.Form):
    login = forms.CharField(label='Nazwa użytkownika',validators=[validate_length],widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nazwa użytkownika'}))
    password = forms.CharField(label='Hasło',widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Hasło'}))
    first_name = forms.CharField(label='Imię',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Imię'}))
    last_name = forms.CharField(label='Nazwisko',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nazwisko'}))
    position = forms.CharField(label='Tytuł lub stopień zawodowy / naukowy',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Tytuł lub stopień zawodowy / naukowy'}))
    phone_number = forms.CharField(label='Numer telefonu',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Numer telefonu'}))
    email = forms.CharField(label='E-mail',validators=[validate_email],widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'E-mail'}))

#class Teacher(forms.ModelForm)
# wybór województw 
vois = (('-','---'),('dolnośląskie','dolnośląskie'),('kujawsko-pomosrkie','kujawsko-pomosrkie'),('lubelskie','lubelskie'),('lubuskie','lubuskie'),('łódzkie','łódzkie'),('małopolskie','małopolskie'),('mazowieckie','mazowieckie'),('opolskie','opolskie'),('podkarpackie','podkarpackie'),('podlaskie','podlaskie'),('pomorskie','pomorskie'),('śląskie','śląskie'),('świętokrzyskie','świętokrzyskie'),('warmińsko-mazurskie','warmińsko-mazurskie'),('wielkopolskie','wielkopolskie'),('zachodniopomorskie','zachodniopomorskie'))
class SchoolForm(forms.Form):
    school = forms.CharField(label='Szkoła pełna nazwa',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nazwa Szkoły'}))
    street = forms.CharField(label='Ulica',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Ulica'}))
    zip_code = forms.CharField(label='Kod pocztowy',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Kod pocztowy'}))
    city = forms.CharField(label='Miasto',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Miasto'}))
    voivodeship = forms.CharField(validators=[validate_],label='Województwo',widget=forms.Select(choices=vois,attrs={'class':'form-control form-control-sm','placeholder':'Województwo'}))
    authority  = forms.CharField(label='Organ prowadzący',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Organ prowadzący'}))
    email = forms.CharField(label='E-mail',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'E-mail'}))
    phone_number = forms.CharField(label='Numer telefonu',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Numer telefonu sekretariatu / dyrekcji'}))
    principal_name = forms.CharField(label='Dyrektor Szkoły',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Imię i nazwisko Dyrektora Szkoły'}))
klasy = (('-','---'),('1','1'),('2','2'),('3','3'),('4','4'))
class StudentForm(forms.Form):
    first_name = forms.CharField(label='Imię',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Imię'}))
    last_name = forms.CharField(label='Nazwisko',widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Nazwisko'}))
    classe = forms.CharField(validators=[validate_],label='Klasa',widget=forms.Select(choices=klasy,attrs={'class':'form-control form-control-sm','placeholder':'Klasa'}))