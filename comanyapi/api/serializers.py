from rest_framework import serializers
from api.models import Company
from api.models import Company,Employee,Image
#Create seriazers here

class CompanySerializer(serializers.ModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    company=CompanySerializer()

    class Meta:
        model=Employee
        fields="__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

class EmployeeSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), required=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'images')

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        employee = Employee.objects.create(**validated_data)
        for image_data in images_data:
            image = Image.objects.create(image=image_data['image'])
            employee.images.add(image)
        return employee

    def create(self, validated_data):
        company_data = validated_data.pop('company')
        company = Company.objects.create(**company_data)
        employee = Employee.objects.create(company=company, **validated_data)
        return employee
