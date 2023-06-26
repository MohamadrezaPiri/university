from django.db import models

# Create your models here.

class Student(models.Model):

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    GRADE_BACHLORE = 'B'
    GRADE_MASTER = 'M'
    
    GRADE_CHOICES = [
        (GRADE_BACHLORE, 'Bachlore'),
        (GRADE_MASTER, 'Master'),
    ]


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default=GENDER_MALE)
    birth_date = models.DateField()
    grade = models.CharField(choices=GRADE_CHOICES, max_length=1, default=GRADE_BACHLORE)
    registration_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=11)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
   
