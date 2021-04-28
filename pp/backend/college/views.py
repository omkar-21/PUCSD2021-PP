from django.shortcuts import render
import json
from college import models, serializers
from django import db,http
from rest_framework import viewsets
# Create your views here.
import datetime

class CourseViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.CourseSerializer
    @classmethod
    def create_course(cls, request):
        value={}
        _err=""
        print(request.data)
        value['name']=request.data['name']
        value['duration']=request.data['duration']
        value['type_of_course']=request.data['type_of_course']
        value['resource']=request.data['resource']
        try:
            with db.transaction.atomic():
         
                entry = models.Courses(name=value['name'],duration=value['duration'],type_of_course=value['type_of_course'],resource=value['resource'])
                entry.save()
                course_id=entry.pk
            status_code=200
        except AssertionError:
            _err="error"
        except db.utils.IntegrityError as err:
            _err="db error" 
        if _err:  
            status_code=400

        return http.JsonResponse(
            {'result': status_code}
        )

    @classmethod
    def list_all_courses(cls, request):
        list = models.Courses.objects.all()
        
        serializer = cls.serializer_class(list,many=True)

        return http.JsonResponse(
            data={
                'data' : serializer.data

            },status=200, safe=False
        )

class CollegeViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.CollegeSerializer
    @classmethod
    def add_college(cls, request):
        value={}
        _err=""
        print(request.data)
        value['name']=request.data['name']
        value['location']=request.data['location']
        value['rank']=request.data['rank']
        value['review']=request.data['review']
        value['courses']=models.Courses.objects.get(id=request.data['courses'])
        try:
            with db.transaction.atomic():
         
                entry = models.College(name=value['name'],location=value['location'],rank=value['rank'],review=value['review'],courses=value['courses'])
                entry.save()
                course_id=entry.pk
                print(course_id)
            status_code=200
        except AssertionError:
            _err="error"
        except db.utils.IntegrityError as err:
            _err="db error" 
        if _err:  
            status_code=400

        return http.JsonResponse(
            {'result': status_code}
        )

    @classmethod
    def list_all_colleges(cls, request):
        list = models.College.objects.all()
        serializer = cls.serializer_class(list,many=True)
        return http.JsonResponse(
            data={
                'data' : serializer.data
            },status=200, safe=False
        )


class ExamViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.ExamSerializer
    @classmethod
    def add_exam(cls, request):
        value={}
        _err=""
        value['name']=request.data['name']
        value['college_name']=models.College.objects.get(id=request.data['college_name'])
        value['exam_date'] = request.data['exam_date']
        value['url'] = request.data['url']
        try:
            with db.transaction.atomic():
         
                entry = models.Exam(url= value["url"],name=value['name'],college_name=value['college_name'],exam_date=value['exam_date'])
                entry.save()
                course_id=entry.pk
            status_code=200
        except AssertionError:
            _err="error"
        except db.utils.IntegrityError as err:
            _err="db error" 
        if _err:  
            status_code=400

        return http.JsonResponse(
            {'result': status_code}
        )

    @classmethod
    def list_all_exams(cls, request):
        list = models.Exam.objects.all()
        serializer = cls.serializer_class(list,many=True)
        final_data=[]

        for exam in serializer.data:
            exam2=models.College.objects.get(id=exam['college_name'])
            exam_serializer = serializers.CollegeSerializer(exam2)
            print(exam_serializer.data['name'])
            
            final_data.append({
                "name" : exam['name'],
                "exam_date" : exam['exam_date'],
                "location" : exam_serializer.data['name'],
                "url" : exam["url"]
            } )


        return http.JsonResponse(
            data={
                'data' : final_data
            },status=200, safe=False
        )

    @classmethod
    def latest_exam(cls, request):
        current_date=datetime.date.today()
        list = latest_post = models.Exam.objects.filter(date__contains=current_date) 
        serializer = cls.serializer_class(list,many=True)
        return http.JsonResponse(
            data={
                'data' : serializer.data[-1]
            },status=200, safe=False
        )
