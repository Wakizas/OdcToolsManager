from rest_framework import generics
from tools_manager.models import Material
from tools_manager.serializers import MaterialSerializer

class MaterialList(generics.ListAPIView):
    serializer_class = MaterialSerializer
    
    def get_queryset(self):
        materials = Material.objects.all()
        return materials