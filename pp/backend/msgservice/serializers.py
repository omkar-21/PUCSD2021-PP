from rest_framework import serializers
from msgservice.models import MsgService

class MsgServiceSerializer(serializers.ModelSerializer):

    class Meta:

        model = MsgService
        fields = '__all__'
