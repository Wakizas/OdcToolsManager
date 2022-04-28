from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from tools_manager.models import Material
from tools_manager.serializers import MaterialSerializer

class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer
    
    def get_queryset(self):
        materials = Material.objects.all()
        return materials