from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
#authentication imports
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#jwt imports
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

@api_view(['GET'])
def api_home(request):
    return Response({'status':200, 'message':'Home Page from Rest_framework'})


class StudentsApi(APIView):
    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students_obj = Student.objects.all()
        seriazer =StudentSerializer(students_obj, many=True)
        return Response({'status':200, 'message':'Student List fetched successfully', 'data': seriazer.data})
    
    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':201, 'message':'Student added successfully', 'data': serializer.data})
        else:
            return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
    
    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data.get('id'))
            serializer = StudentSerializer(student_obj, data=request.data)
            if not serializer.is_valid():
                return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
            serializer.save() 
            return Response({'status':200, 'message':'Student updated successfully', 'data': serializer.data})
        except Student.DoesNotExist:
            return Response({'status':404, 'message':'Student not found'})
        
    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data.get('id'))
            serializer = StudentSerializer(student_obj, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
            serializer.save()
            return Response({'status':200, 'message':'Student partially updated successfully', 'data': serializer.data})
        except Student.DoesNotExist:
            return Response({'status':404, 'message':'Student not found'})
        
    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data.get('id'))
            student_obj.delete()
            return Response({'status':200, 'message':'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'status':404, 'message':'Student not found'})

from rest_framework_simplejwt.tokens import RefreshToken
class Registration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': 201,
                'message': 'User registered successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'data': serializer.data
            })
        
        return Response({
            'status': 400,
            'message': 'Bad Request',
            'errors': serializer.errors
        })














# @api_view(['GET'])
# def student_list(request):
#     students_obj = Student.objects.all()
#     seriazer =StudentSerializer(students_obj, many=True)
#     return Response({'status':200, 'message':'Student List fetched successfully', 'data': seriazer.data})

# @api_view(['POST'])
# def add_student(request):
#     data = request.data
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status':201, 'message':'Student added successfully', 'data': serializer.data})
#     else:
#         return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
    
# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data)
#         if not serializer.is_valid():
#             return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
#         serializer.save() 
#         return Response({'status':200, 'message':'Student updated successfully', 'data': serializer.data})
#     except Student.DoesNotExist:
#         return Response({'status':404, 'message':'Student not found'})

# @api_view(['PATCH'])
# def patial_update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             return Response({'status':400, 'message':'Bad Request', 'errors': serializer.errors})
#         serializer.save()
#         return Response({'status':200, 'message':'Student partially updated successfully', 'data': serializer.data})
#     except Student.DoesNotExist:
#         return Response({'status':404, 'message':'Student not found'})
    
# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         student_obj.delete()
#         return Response({'status':200, 'message':'Student deleted successfully'})
#     except Student.DoesNotExist:
#         return Response({'status':404, 'message':'Student not found'})
    
@api_view(['GET'])
def api_books(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many=True)
    return Response({'status':200, 'message':'Book List fetched successfully', 'data': serializer.data})