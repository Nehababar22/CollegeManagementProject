from django.contrib.auth.models import User
from rest_framework import routers
from CMS_app import views

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'Department', views.DepartmentViewSet)
router.register(r'UserProfile', views.UserProfileViewSet)
router.register(r'Attendance', views.AttendanceViewSet)
router.register(r'Leaves', views.LeavesViewSet)
router.register(r'Salary', views.SalaryViewSet)
router.register(r'Fees', views.FeesViewSet)

