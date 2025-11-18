from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #fields = ['name', 'age', 'enrollment_date'] or exclude = ['enrollment_date'] or
        fields = '__all__' 
