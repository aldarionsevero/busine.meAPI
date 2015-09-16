from authentication.models import BusinemeUser
from django.test import SimpleTestCase
from django.http import HttpResponse


STATUS_NOT_FOUND = 404


class BusinemeUserAuth(SimpleTestCase):

    def create_user(self, request):
        """PUT method for create an user by receiving
        four arguments from application, using POST method for security"""

        new_user = BusinemeUser()
        new_user.username = request.POST['username']
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.set_password(request.POST['password'])

        # Must check if the assertives is  write correcly and define a message
        # error for each one

        username = new_user.username
        first_name = new_user.first_name
        last_name = new_user.last_name

        new_user.assertIsNone(username)
        new_user.assertIsNone(first_name)
        new_user.assertIsNone(last_name)

        new_user.assertEquals(username, '')
        new_user.assertEquals(first_name, '')
        new_user.assertEquals(last_name, '')

        new_user.save()

    def update_user_first_last_name(self, request):
        """Define method for update first_name and last_name given a
           specific BuslineUser using the POST method for security"""

        update_user = request.user
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']

        first_name = update_user.first_name
        last_name = update_user.last_name

        update_user.assertIsNone(update_user)
        update_user.assertIsNone(first_name)
        update_user.assertIsNone(last_name)

        update_user.assertEquals(first_name, '')
        update_user.assertEquals(last_name, '')

        update_user.save()

    def update_user_password(self, request):

        update_user = request.user

        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        update_user.assertNotEquals(new_password, None)
        update_user.assertNotEquals(confirm_new_password, None)

        if new_password.isEquals(confirm_new_password):
            update_user.set_password(new_password)
            update_user.save()

            message_log_sucess = "Changes saved"
            response = HttpResponse(message_log_sucess)
        else:
            message_log_fail = "Unable to change password \
                                password's don't match"
            response = HttpResponse(message_log_fail)

        return response
