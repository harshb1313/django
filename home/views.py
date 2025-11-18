from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

@api_view(['GET'])
def api_home(request):
    return Response({'status':'200', 'message':'Home Page from Rest_framework'})

@api_view(['GET'])
def student_list(request):
    students_objs = Student.objects.all()
    serializer = StudentSerializer(students_objs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status':'201', 'message':'Student added successfully', 'data': serializer.data})
    else:
        return Response({'status':'400', 'message':'Bad Request', 'errors': serializer.errors})