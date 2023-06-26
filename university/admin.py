from django.contrib import admin
from .models import Student, Address

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
