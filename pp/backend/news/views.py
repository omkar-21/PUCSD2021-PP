from django.shortcuts import render
import datetime
import json
from news import models, serializers
from django import db,http
from rest_framework import viewsets

# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.NewsSerializer
    @classmethod
    def add_news(cls, request):
        value={}
        _err=""
        value['heading']=request.data['heading']
        value['news']=request.data['news']
        try:
            with db.transaction.atomic():
                entry = models.News(heading=value['heading'],news=value['news'])
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
    def list_all_news(cls, request):
        list = models.News.objects.all()
        serializer = cls.serializer_class(list,many=True)
        return http.JsonResponse(
            data={
                'data' : serializer.data
            },status=200, safe=False
        )

    @classmethod
    def latest_news(cls, request):
        current_date=datetime.date.today()
        list = latest_post = models.News.objects.filter(date__contains=current_date) 
        serializer = cls.serializer_class(list,many=True)
        return http.JsonResponse(
            data={
                'data' : serializer.data[-1]
            },status=200, safe=False
        )
