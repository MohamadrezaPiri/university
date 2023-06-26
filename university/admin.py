from django.contrib import admin
from .models import Student, Address

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','gender','birth_date','grade','registration_date','graduation_date','phone']
