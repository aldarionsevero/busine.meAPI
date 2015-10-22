from django import forms
from .models import BusinemeUser

"""
This class is used for change BusinemeUser in model.
"""

class BusinemeUserForm(forms.ModelForm):

    """
    Meta is a abstract class of BusinemeUser used for create tables in database
    """

    class Meta:
        model = BusinemeUser
        fields = ('first_name', 'username', 'email', 'password')
