

class Serializer():

    def serialize(self, busineme_object):
        """ This method generate json based in the fields who we want to
                show or we user in the aplicattion.

                busineme_object is a generic object
                which we want to see their values """

        required_fields = busineme_object.serialize_fields
        json_fields = {}

        for fields in required_fields:

            json_fields[fields] = getattr(user, fields)

        return json_fields
