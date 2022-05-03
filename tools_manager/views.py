<<<<<<< HEAD
from rest_framework.viewsets import ModelViewSet
from tools_manager.models import Material, MaterialType, Entity, EntityType
from tools_manager.serializers import MaterialSerializer, MaterialTypeSerializer, EntitySerializer, EntityTypeSerializer

=======
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tools_manager.models import Material, User
from tools_manager.serializers import MaterialSerializer, UserSerializer
>>>>>>> laya

class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        materials = Material.objects.all()
        return materials

<<<<<<< HEAD

class MaterialTypeViewSet(ModelViewSet):
    serializer_class = MaterialTypeSerializer

    def get_queryset(self):
        materials = MaterialType.objects.all()
        return materials


class EntityViewSet(ModelViewSet):
    serializer_class = EntitySerializer

    def get_queryset(self):
        entity = Entity.objects.all()
        return entity


class EntityTypeViewSet(ModelViewSet):
    serializer_class = EntityTypeSerializer

    def get_queryset(self):
        entity = EntityType.objects.all()
        return entity
=======
class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    
    def get_queryset(self):
        users = User.objects.all()
        return users
            
>>>>>>> laya
