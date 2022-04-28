# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    entity_type = models.ForeignKey('EntityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'entity'


class EntityType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'entity_type'


class Material(models.Model):
    name = models.CharField(max_length=200)
    characteristics = models.CharField(max_length=255, blank=True, null=True)
    equipment_condition = models.CharField(max_length=100, blank=True, null=True)
    entity = models.ForeignKey(Entity, models.DO_NOTHING)
    material_type = models.ForeignKey('MaterialType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material'


class MaterialRequest(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    quantity = models.IntegerField()
    request = models.ForeignKey('Request', models.DO_NOTHING)
    material = models.ForeignKey(Material, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'material_request'


class MaterialType(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'material_type'


class Request(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    material = models.ForeignKey(Material, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'request'


class User(models.Model):
    id_number = models.CharField(unique=True, max_length=8)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=10, blank=True, null=True)
    picture = models.TextField(blank=True, null=True)
    user_type = models.ForeignKey('UserType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'


class UserType(models.Model):
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_type'
