from django.db import models
from django.contrib.auth.models import AbstractUser


def serialize(busineme_object):
    """
    This method generate json based in the fields who we want to
    show or we user in the aplicattion. Busineme_object is a generic object
    which we want to see their values.
    """
    required_fields = busineme_object.serialize_fields
    json_dict = {}

    for fields in required_fields:
        attribute = getattr(busineme_object, fields)
        if issubclass(attribute.__class__, models.Model) \
                or issubclass(attribute.__class__, AbstractUser):
            json_dict[fields] = serialize(attribute)
        else:
            json_dict[fields] = attribute
    return json_dict


def serialize_objects(object_list):
    json_dict = {}
    json_list = []
    for object in object_list:
        json_list.append(serialize(object))
    json_dict["objects"] = json_list
    return json_dict
