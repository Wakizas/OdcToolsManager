from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tools_manager.models import Material, User
from tools_manager.serializers import MaterialSerializer, UserSerializer

class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer
    
    def get_queryset(self):
        materials = Material.objects.all()
        return materials

class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    
    def get_queryset(self):
        users = User.objects.all()
        return users
            