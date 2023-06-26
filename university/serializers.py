from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','first_name','last_name','birth_date','gender','grade','registration_date','graduation_date','address','phone']
        