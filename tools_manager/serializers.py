from rest_framework import serializers
from tools_manager.models import Material, MaterialType, Entity, EntityType, UserType, User


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['entity_type'] = EntityTypeSerializer(instance.entity_type).data
        return representation


class MaterialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialType
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['entity'] = EntitySerializer(instance.entity).data
        representation['material_type'] = MaterialTypeSerializer(instance.material_type).data
        return representation

    def create(self, validated_data):
        return Material.objects.create(**validated_data)


class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserType
        fields =  '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user_type'] = UserTypeSerializer(instance.user_type).data
        return representation
