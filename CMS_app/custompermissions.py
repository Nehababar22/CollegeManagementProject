from rest_framework import permissions

class MyPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view,obj):        
        if request.method in ['POST','GET']:
            return True
        elif request.method in ['PUT','DELETE','PATCH']:
            print(obj.user.id)
            print(request.user.id)
            return  obj.user.user == request.user
        else:
            return False
     

       
