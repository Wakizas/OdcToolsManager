from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Entity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    entity_type = models.ForeignKey('EntityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entity'

    def __str__(self):
        return self.name


class EntityType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'entity_type'

    def __str__(self):
        return self.label


class Material(models.Model):
    name = models.CharField(max_length=200)
    characteristics = models.CharField(max_length=500, blank=True, null=True)
    equipment_condition = models.CharField(
        max_length=100, blank=True, null=True)
    entity = models.ForeignKey(Entity, models.DO_NOTHING)
    material_type = models.ForeignKey('MaterialType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material'


class MaterialType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'material_type'

    def __str__(self):
        return self.label


class User(AbstractBaseUser):
    id_number = models.CharField(unique=True, max_length=8)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(
        unique=True, max_length=10, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    user_type = models.ForeignKey('UserType', models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    last_login = models.DateField()
    email = models.EmailField(unique=True, max_length=254)

    USERNAME_FIELD = 'email'

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.id_number
       

class UserMaterial(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    material = models.ForeignKey(Material, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_material'


class UserType(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type'
    def __str__(self):
        return self.label
    