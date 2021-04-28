from rest_framework import serializers
from college.models import Courses, College, Exam

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Courses
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = College
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'