from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import Group
import datetime
from pagedown.widgets import AdminPagedownWidget
phone_regex = RegexValidator(regex=r'^\d{5,15}$', message="Wprowadź prawidłowy numer telefonu")
email_regex = RegexValidator(regex=r'^[\w.-]+@[\w.-]+.\w+$', message="Wprowadź prawidłowy numer telefonu")
# Create your models here.
class School(models.Model):
    school = models.CharField('Szkoła pełna nazwa', max_length=100)
    street = models.CharField('Ulica', max_length=100)
    zip_code = models.CharField('Kod pocztowy', max_length=6)
    city = models.CharField('Miasto', max_length=100)
    voivodeship = models.CharField('Województwo', max_length=100)
    authority = models.CharField('Organ prowadzący', max_length=100)
    phone_number = models.CharField('Numer telefonu sekretariatu / dyrekcji',validators=[phone_regex], max_length=17) 
    email = models.CharField('Adres email sekretariatu',validators=[email_regex], max_length=50, blank=False) 
    principal_name = models.CharField('Imię i nazwisko Dyrektora Szkoły', max_length=50, blank=True)
    class Meta:
        verbose_name = "Szkoła"
        verbose_name_plural = "Szkoły"

    def __unicode__(self):
        return self.school
    def __str__(self):
        return self.school
class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField('Imię',max_length=100)
    last_name = models.CharField('Nazwisko',max_length=100)
    position = models.CharField('Tytuł lub stopień zawodowy / naukowy',max_length=100)
    phone_no = models.IntegerField('Telefon kontaktowy')
    email =models.CharField('Adres email sekretariatu',validators=[email_regex], max_length=50, blank=False, default='adres@szkola.pl') 
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    obj_key = models.CharField('Klucz obiektu', max_length=50, blank=True) 
    obj_state = models.CharField('Status obiektu', max_length=50, blank=True) 
    class Meta:
        verbose_name = "Nauczyciel"
        verbose_name_plural = "Nauczyciele"

    def __unicode__(self):
        return self.first_name+' '+self.last_name
    def __str__(self):
        return self.first_name+' '+self.last_name
class Article(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateField('Data utworzenia',auto_now_add=True, blank=True)
    modification_date = models.DateField('Data modyfikacji', auto_now_add=True, blank=True)
    title = models.CharField('Tytuł', max_length=100, blank=False)
    lead = models.CharField('Lead', max_length=300, blank=True)
    text = models.TextField('Tekst artykułu', blank=False)
    tags = models.CharField('tagi', max_length=500, blank=True)
    position = models.CharField('Umieść na stronie', max_length=100, blank=True)
    class Meta:
        verbose_name = "Artykuł"
        verbose_name_plural = "Artykuły"

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
class Student(models.Model):
    first_name = models.CharField('Imię',max_length=100)
    last_name = models.CharField('Nazwisko',max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    classe = models.CharField('Klasa',max_length=100)
    email =models.CharField('Adres email',validators=[email_regex], max_length=50, blank=False, default='uczen@szkola.pl') 
    obj_key = models.CharField('Klucz obiektu', max_length=50, blank=True) 
    
    class Meta:
        verbose_name = "Uczeń"
        verbose_name_plural = "Uczniowie"

    def __unicode__(self):
        return self.first_name+' '+self.last_name
    def __str__(self):
        return self.first_name+' '+self.last_name
class Acceptance(models.Model):
    title = models.CharField('Tytuł', max_length=100, blank=False)
    text = models.TextField('Tekst oświadczenia', blank=False)
    required = models.BooleanField('Wymagana?')
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Zgoda"
        verbose_name_plural = "Zgody"

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title