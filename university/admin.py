from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','gender','birth_date','grade','registration_date','graduation_date','address','phone']
    list_display = ['first_name','last_name','birth_date','grade','registration_date','graduation_date','phone']
    list_filter = ['gender','grade']
    list_per_page = 10
    search_fields = ['last_name']