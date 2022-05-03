from rest_framework import serializers
from tools_manager.models import Material, UserType, User


class MaterialSerializer(serializers.ModelSerializer):
    material_type_label = serializers.CharField(source='material_type.label', read_only=True)
    entity_name = serializers.CharField(source='entity.name', read_only=True)
    class Meta:
        model = Material
        fields = ['name', 'characteristics', 'equipment_condition', 'material_type_label', 'entity_name']


class UserTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserType
        fields =  '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
    '''
    def to_representation(self, instance):

            Permet de retourner tous les champs de UserType en plus de l'id
        
        representation = super().to_representation(instance)
        representation['user_type'] = UserTypeSerializer
        return representation

'''