"""
Busine-me API
Universidade de Brasilia - FGA
Técnicas de Programação, 2/2015
@file serializers.py
Methods to serialize objects.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


def serialize(busineme_object):
    """
    This method generate json based in the field who we want to
    show or we user in the aplicattion. Busineme_object is a generic object
    which we want to see their values.
    """
    required_fields = busineme_object.serialize_fields
    json_dict = {}

    for field in required_fields:
        attribute = getattr(busineme_object, field)
        if issubclass(attribute.__class__, models.Model) \
                or issubclass(attribute.__class__, AbstractUser) \
                or issubclass(attribute.__class__, models.Manager):
            if issubclass(attribute.__class__, models.Manager):
                json_dict[field] = serialize_list(attribute)
            else:
                json_dict[field] = serialize(attribute)
        else:
            json_dict[field] = attribute
    return json_dict


def serialize_objects(object_list):
    """
    Convert objects in json.
    """
    json_dict = {}
    json_list = []
    for object in object_list:
        json_list.append(serialize(object))
    json_dict["objects"] = json_list
    return json_dict


def serialize_list(many_to_many_field):
    """
    Convert lists in json.
    """
    object_list = many_to_many_field.all()
    json_list = []
    for object in object_list:
        json_list.append(serialize(object))
    return json_list
