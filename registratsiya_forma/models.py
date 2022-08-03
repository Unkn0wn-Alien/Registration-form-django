from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    area_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    exist =models.CharField(max_length=3)

    class Meta():
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f'{self.first_name}' + ' ' + f'{self.last_name}'