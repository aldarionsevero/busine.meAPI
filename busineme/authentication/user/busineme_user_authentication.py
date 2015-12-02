"""
Busine-me API
Universidade de Brasilia - FGA
Tecnicas de Programacao, 2/2015
@file models.py
Model for user authentication.
"""
from authentication.models import BusinemeUser


def create_user(request):
    """PUT method for create an user by receiving
    four arguments from application."""

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

    new_user.assertEquals(username, None)
    new_user.assertEquals(first_name, None)
    new_user.assertEquals(last_name, None)

    new_user.assertEquals(username, '')
    new_user.assertEquals(first_name, '')
    new_user.assertEquals(last_name, '')

    new_user.save()


def update_user_first_last_name(request):
    """Define method for update first_name and last_name given a
       specific BuslineUser using the POST method for security"""

    update_user = request.user
    update_user.first_name = request.POST['first_name']
    update_user.last_name = request.POST['last_name']

    first_name = update_user.first_name
    last_name = update_user.last_name

    update_user.assertEquals(first_name, None)
    update_user.assertEquals(last_name, None)

    update_user.save()


def update_user_password(request):
    """Define method for update password attribute given a
        specific BuslineUser using the POST method for security"""

    update_user = request.user
    update_user_password.set_password(request.POST['password'])

    password = update_user_password
    update_user.assertEquals(password, None)
    update_user.assertEquals(password, '')
    update_user.save()
