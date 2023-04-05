from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import csv 
from CMS_app.models import Department,UserProfile

class Command(BaseCommand):
    help = 'Create random users'
    
    
    def handle(self, *args, **options):
       
        with open('C:/Users/HP/CollegeManagementSystem/CMS_Project/CMS_app/management/commands/user_info.csv') as csvfile:
          reader = csv.DictReader(csvfile) 
    
          for row in reader:
            existing_user = User.objects.filter(username = row['username'])
            if not existing_user :
                user = User(first_name = row['first_name'], last_name = row['last_name'], username = row['username'], email = row['email'] )         
                user.save()      
                department,created = Department.objects.get_or_create(name = row['department']) 
                t = UserProfile.objects.get(user = user)
                t.contact = row['contact']
                t.role = row['role']
                t.department =department
                t.save() 








 
