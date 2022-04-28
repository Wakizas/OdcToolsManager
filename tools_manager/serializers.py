from rest_framework import serializers
from tools_manager.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    material_type_label = serializers.CharField(source='material_type.label', read_only=True)
    entity_name = serializers.CharField(source='entity.name', read_only=True)
    class Meta:
        model = Material
        fields = ['name', 'characteristics', 'equipment_condition', 'material_type_label', 'entity_name']