from os import name
from django.db.models import fields
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import  serializers

from CMS_app.models import  Department, UserProfile,Attendance, Leaves, Salary, Fees

#serializer define the API representation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','is_staff']
       # fields ='__all__'
              
class DepartmentSerializer(serializers.ModelSerializer):
    
    class  Meta:
          model = Department
          #fields =['name']
          fields = "__all__"
                    
class UserProfileSerializer(serializers.ModelSerializer):
      user_details = serializers.SerializerMethodField()
      def get_user_details(self,obj):
          results = User.objects.filter(user=obj)
          list = []
          for i in results:
              dict = {
              'id':i.id,
              'username': i.username,
              'first_name':i.first_name,
              'last_name': i.last_name,
              'email': i.email,  
              }  
          list.append(dict)
          return list    
        
      class  Meta:
          model = UserProfile
          #fields = ['user','contact', 'department','role']  
          fields = "__all__"       
          
class AttendanceSerializer(serializers.ModelSerializer):
    class  Meta:
          model = Attendance
         # fields =['user','date']   
          fields = "__all__"   
          
class LeavesSerializer(serializers.ModelSerializer):
    class  Meta:
          model = Leaves
          #fields = ['user','title','description', 'leave_apply_date','leave_start_date','leave_end_date'] 
          fields = "__all__"
          
class SalarySerializer(serializers.ModelSerializer):
    class  Meta:
          model = Salary
          #fields = ['teacher','salary_month','salary_credited_on','amount']    
          fields = "__all__"
          
class FeesSerializer(serializers.ModelSerializer):

    class  Meta:
          model = Fees
          #fields = ['student','amount','fees_paid_on', 'description']    
          fields = "__all__"                  
