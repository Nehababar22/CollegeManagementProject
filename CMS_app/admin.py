from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.models import User

from CMS_app.models import Attendance, Department, Fees, Leaves, Salary, UserProfile

# Register your models here. 

admin.site.register(Department)
admin.site.register(UserProfile)
admin.site.register(Attendance)
admin.site.register(Leaves)
admin.site.register(Salary)
admin.site.register(Fees)
