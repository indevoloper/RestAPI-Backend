from rest_framework import serializers
from .models import app

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = app
        fields = ('id', 'username', 'lastname', 'age','weight','gender')