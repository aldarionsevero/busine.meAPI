from django.test import TestCase
from ..models import Busline
from ..models import Terminal
from ..models import Favorite
from authentication.models import BusinemeUser

"""
This class is used for create tests some validations in Busline class.
"""


class TestBusline(TestCase):

    def setUp(self):
        self.busline = Busline()

        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    def test_str(self):
        self.assertEquals(
            "001 - route", self.busline.__str__())

    """
    This test method is used for analysis if the filter of the number lines
    is properly executed.
    """

    def test_filter_by_line_number(self):
        bus = self.busline.api_filter_startswith('001')
        self.assertEquals(bus[0], self.busline)


"""
This class is used for testing the Favorite model.
"""


class TestFavorite(TestCase):

    def setUp(self):
        self.favorite = Favorite()

        self.user = BusinemeUser()
        self.user.username = "TestUser"
        self.user.save()

        self.busline = Busline()
        self.busline.line_number = "001"
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()

        self.favorite.user = self.user
        self.favorite.busline = self.busline
        self.favorite.save()

    def test_str(self):
        self.assertEquals(
            "testuser - 001", self.favorite.__str__())
