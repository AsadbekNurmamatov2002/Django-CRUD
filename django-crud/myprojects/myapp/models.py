from django.db import models

# Create your models here.

class Student(models.Model):
    ism =models.CharField(max_length=120, help_text='ism')
    familya=models.CharField(max_length=120)
    manzil=models.CharField(max_length=150)
    mamlakat=models.CharField(max_length=150)
    yoshi=models.IntegerField()
    def __str__(self):
        return self.ism
    ordering=['ism'] 