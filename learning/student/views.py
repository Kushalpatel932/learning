from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from student.serializers import UserDataSerializer,GetUsersSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from rest_framework import permissions, viewsets

class CreateUserData(APIView):
    @csrf_exempt
    def post(self,request):
        data= request.data
        print("data-------------------------{}".format(data))
        serializer =UserDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class GetUsersDate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GetUsersSerializer
    # def get(self,request):
    #     users= User.objects.all()
    #     serializer_class= GetUsersSerializer
        


