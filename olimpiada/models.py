from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField('Imię',max_length=100)
    last_name = models.CharField('Nazwisko',max_length=100)
    position = models.CharField('Tytuł lub stopień zawodowy / naukowy',max_length=100)
    phone_no = models.IntegerField('Telefon kontaktowy')
    class Meta:
        verbose_name = "Nauczyciel"
        verbose_name_plural = "Nauczyciele"

    def __unicode__(self):
        return self.name
class School(models.Model):
    school = models.CharField('Szkoła pełna nazwa', max_length=100)
    street = models.CharField('Ulica', max_length=100)
    zip_code = models.CharField('Kod pocztowy', max_length=6)
    city = models.CharField('Miasto', max_length=100)
    voivodeship = models.CharField('Województwo', max_length=100)
    authority = models.CharField('Miasto', max_length=100)
    class Meta:
        verbose_name = "Szkoła"
        verbose_name_plural = "Szkoły"

    def __unicode__(self):
