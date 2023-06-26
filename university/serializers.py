from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name','last_name','birth_date','grade','registration_date','graduation_date','phone']
        