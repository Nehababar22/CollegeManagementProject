from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from rest_framework import  filters
import django_filters.rest_framework
from .Pagination import MyPageNumberPagination
from .custompermissions import MyPermission
from CMS_app.serializers import UserSerializer, DepartmentSerializer, UserProfileSerializer, AttendanceSerializer, LeavesSerializer,SalarySerializer ,FeesSerializer  
from CMS_app.models import Attendance, Department, Attendance, Fees, Leaves, Salary, UserProfile


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
        
class DepartmentViewSet(viewsets.ModelViewSet, ):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MyPageNumberPagination

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
       t = UserProfile.objects.all()
       qs = t.filter(user=self.request.user)
       return qs
      
       
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
                    
class LeavesViewSet(viewsets.ModelViewSet):
    queryset = Leaves.objects.all()
    serializer_class = LeavesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id']
    permission_classes = [MyPermission]
    
    
class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer 
    permission_classes = [IsAuthenticated]
    
class FeesViewSet(viewsets.ModelViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer
    permission_classes = [IsAuthenticated]
