from django.db import models
from django.contrib.auth.models import AbstractUser


def serialize(busineme_object):
    """
    This method generate json based in the fields who we want to
    show or we user in the aplicattion. Busineme_object is a generic object
    which we want to see their values.
    """
    required_fields = busineme_object.serialize_fields
    json_fields = {}

    for fields in required_fields:
        if not issubclass(fields.__class__, models.Model) and \
                issubclass(fields.__class__, AbstractUser):
            json_fields[fields] = getattr(busineme_object, fields)
        else:
            serialize(fields)
    return json_fields


def serialize_users(user_list):
    json_fields = {}
    for user in user_list:
        json_fields[user.username] = serialize(user)
    return json_fields
