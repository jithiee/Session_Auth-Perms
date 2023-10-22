from django.shortcuts import render
from rest_framework import viewsets
from . models import Student
from . sserializer import StudentSerializer
# from rest_framework.authentication import BasicAuthentication   # there is dirctily going to login page
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


class StudentModelViewApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer
    authentication_classes = [ SessionAuthentication]
    # permission_classes = [IsAuthenticated]     
    # permission_classes = [IsAuthenticatedOrReadOnly]   # this used for IsAuthenticated  Or   ReadOnly
    permission_classes = [DjangoModelPermissions] #this used for we can permission to the user through the adminpannel 
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    



