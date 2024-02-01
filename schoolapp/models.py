from django.db import models


# Create your models here.
class DEPARTMENT(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def  __str__(self):
        return self.name


class Student(models.Model):
     name1 = models.CharField(max_length=250)
     DOB = models.DateField()
     age = models.IntegerField()
     gender = models.TextField(max_length=10)
     phonenumber = models.IntegerField()
     email = models . EmailField()

     class Meta:
         ordering = ('name1',)
         verbose_name = 'student'
         verbose_name_plural = 'students'
     def __str__(self):
         return self.name1



