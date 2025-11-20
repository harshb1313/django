from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):

    # def validate_age(self, value):
    #     if value<18:
    #         raise serializers.ValidationError({'error':'age must be grater than 18'})
    #     return value
    # def validate_phoneNumber(self, value):
    #     if value and len(value) != 10:
    #         raise serializers.ValidationError({'error':'number must be 10 digits'})
    #     return value
    #field level validation name the function as u have named the field in model

    def validate(self, data):
    # Validate age only if provided (PATCH-safe)
        age = data.get('age')
        if age is not None and age < 18:
            raise serializers.ValidationError({'error': 'age must be greater than 18'})

    # Validate name only if provided (PATCH-safe)
        name = data.get('name')
        if name is not None:
            for char in name:
                if not char.isalpha() and char != ' ':
                    raise serializers.ValidationError({'error': 'name must contain only alphabets'})
        return data

    class Meta:
        model = Student
        #fields = ['name', 'age', 'enrollment_date'] or exclude = ['enrollment_date'] or
        fields = '__all__' 

       

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)

    


class BookSerializer (serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'
    #  class Meta:
    #     model = Book
    #     fields = '__all__'
    #     depth = 1 #to show related model data
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User,
        fields = ['username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    #for hashing password