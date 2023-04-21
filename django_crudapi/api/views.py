from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from api.serializers import StudentSerializer
from api.models import Student


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDeleteAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer