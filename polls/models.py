from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField('Imię',max_length=100)
    last_name = models.CharField('Nazwisko',max_length=100)
    position = models.CharField('Tytuł lub stopień zawodowy / naukowy',max_length=100)
    phone_no models.IntegerField('Telefon kontaktowy')
    class Meta:
        verbose_name = "Nauczyciel"
        verbose_name_plural = "Nauczyciele"

    def __unicode__(self):
        return self.name