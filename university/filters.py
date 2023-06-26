from django_filters.rest_framework.filterset import FilterSet
from .models import Student

class StudentFilters(FilterSet):
    class Meta:
        model = Student
        fields = {
            'gender': ['exact'],
            'grade': ['exact'],
        }
