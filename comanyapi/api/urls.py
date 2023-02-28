from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet,EmployeeImageUpload
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'Employee',EmployeeViewSet)


urlpatterns = [
    
    path('',include(router.urls)),
    path('employees/upload/', EmployeeImageUpload.as_view()),
]

