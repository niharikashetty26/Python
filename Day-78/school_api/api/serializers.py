from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'courses']

    def create(self, validated_data):
        courses_data = validated_data.pop('courses')
        student = Student.objects.create(**validated_data)
        for course_data in courses_data:
            course, created = Course.objects.get_or_create(**course_data)
            student.courses.add(course)
        return student

    def update(self, instance, validated_data):
        courses_data = validated_data.pop('courses')
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.enrollment_date = validated_data.get('enrollment_date', instance.enrollment_date)
        instance.save()

        instance.courses.clear()
        for course_data in courses_data:
            course, created = Course.objects.get_or_create(**course_data)
            instance.courses.add(course)

        return instance

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username', 'password', 'email']
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

