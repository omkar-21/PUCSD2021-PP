from django.shortcuts import render
import json
from django import db,http

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Users.serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserLogoutViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    @classmethod
    def logout_user(cls, request):
        logout(request)
        return http.JsonResponse(
            {'result': "logout"}
        )

