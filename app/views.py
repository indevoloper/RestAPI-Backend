from django.shortcuts import render
from rest_framework import viewsets
from .serializers import appSerializer
from .models import app



class appView(viewsets.ModelViewSet):
    serializer_class = appSerializer
    queryset = app.objects.all()
