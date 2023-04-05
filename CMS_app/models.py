from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40,unique=True)
        
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='user')
    contact = models.CharField(max_length=10)
    department = models.ForeignKey(Department,on_delete=models.CASCADE, null = True)
    role = models.CharField(max_length=50)
    
    def __str__(self):
       return str(self.user)
      
    def create_UserProfile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)   
    post_save.connect(create_UserProfile,sender = User)  
      
    
class Attendance(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
class Leaves(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    leave_apply_date = models.DateField(auto_now_add=True)
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    
class Salary(models.Model):
    teacher = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    salary_month = models.CharField(max_length=10)
    salary_credited_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    
class Fees(models.Model):
    student = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    amount  = models.IntegerField()
    fees_paid_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

   
  

            
