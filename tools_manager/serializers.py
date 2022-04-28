from rest_framework import serializers
from tools_manager.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    material_type = serializers.CharField(source='material_type')
    entity = serializers.CharField(source='entity')
    class Meta:
        model = Material
        fields = ['name', 'charateristics', 'equipment_condition', 'material_type', 'entity']