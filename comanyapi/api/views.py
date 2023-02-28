from django.forms import ValidationError
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import status


class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer      
def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))                          
class EmployeeImageUpload(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def upload_files(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        files = request.FILES.getlist('files')
        # Do something with the uploaded files
        for file in files:
            # Save the file to the server or process it in some way
            pass
        # Redirect back to the form page
        return HttpResponseRedirect(reverse('upload_files'))
    else:
        return render(request, 'upload_files')

class MyViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            print(e.detail) # print validation errors for debugging
            raise e

