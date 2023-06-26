from django.contrib import admin
from .models import Student, Address

# Register your models here.

class AddressInline(admin.TabularInline):
    min_num = 1
    max_num = 1
    model = Address
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name','last_name','gender','birth_date','grade','registration_date','graduation_date','phone']
