from django.db import models


def serialize(busineme_object):
    """
    This method generate json based in the fields who we want to
    show or we user in the aplicattion. Busineme_object is a generic object
    which we want to see their values.
    """
    required_fields = busineme_object.serialize_fields
    json_fields = {}

    for fields in required_fields:
        if not issubclass(fields.__class__, models.Model):
            json_fields[fields] = getattr(busineme_object, fields)
        else:
            serialize(fields)
    return json_fields
