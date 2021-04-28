from django.shortcuts import render
import json
from msgservice import models, serializers
from django import db,http
from rest_framework import viewsets

# Create your views here.
class MsgServiceViewSet(viewsets.ModelViewSet):
    
    serializer_class=serializers.MsgServiceSerializer
    @classmethod
    def register_service(cls, request):
        value={}
        _err=""
        print(request.data)
        value['email_id']=request.data['email_id']
        value['mobile_no']=request.data['mobile_no']
        try:
            with db.transaction.atomic():
                entry = models.MsgService(email_id=value['email_id'],mobile_no=value['mobile_no'])
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
    def users(cls, request):
        list = models.MsgService.objects.all()
        serializer = cls.serializer_class(list,many=True)
        return http.JsonResponse(
            data={
                'data' : serializer.data
            },status=200, safe=False
        )
