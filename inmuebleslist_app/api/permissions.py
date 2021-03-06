from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    #esta funcion devuelve un bool siempre
    def has_permission(self, request, view):
        
        if request.method == 'GET':
            return True
        
        staff_permission = bool(request.user and request.user.is_staff)
        return staff_permission
    

#Si el comentario es mio lo puedo manipular, sino solo verlo
class IsComentario_UserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.comentario_user == request.user or request.user.is_staff