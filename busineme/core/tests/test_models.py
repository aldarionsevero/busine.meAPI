from django.test import TestCase
from ..models import Busline
from ..models import Terminal
from ..models import Favorite
from ..models import Company
from ..models import Post
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

    def test_filter_by_line_description(self):
        bus = self.busline.filter_by_line_description("001", "route")
        self.assertEquals(1, bus.count())


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


class TestCompany(TestCase):

    def setUp(self):
        self.company = Company()

        self.company.name = "CompanyTestName"
        self.company.save()

    def test_str(self):
        self.assertEquals(
            "CompanyTestName", self.company.__str__())


class TestTerminal(TestCase):

    def setUp(self):
        self.terminal = Terminal()

        self.terminal.description = "Terminal Description Test String"
        self.terminal.addres = "Terminal Adress Test String "
        self.terminal.save()

    def test_str(self):
        self.assertEquals(
            "Terminal Description Test String", self.terminal.__str__())


class TestPost(TestCase):

    def setUp(self):
        self.post = Post()

        self.busline = Busline()
        self.busline.line_number = "001"
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.busline.save()

        self.user = BusinemeUser()
        self.user.username = "TestUser"
        self.user.save()

        self.post.busline = self.busline
        self.post.traffic = 1
        self.post.capacity = 1
        self.post.user = self.user
        self.post.save()
        self.date_now = self.post.date
        self.time_now = self.post.time

    def test_str(self):
        self.assertEquals(
            "id: 1 date: %s %s busline_id: 1" % (self.date_now, self.time_now),
            self.post.__str__())

    def test_api_all(self):
        self.assertEquals(1, self.post.api_all().count())

    def test_api_filter_contains(self):
        busline = self.busline
        self.assertEquals(1, self.post.api_filter_contains(busline).count())

    # def test_api_get(self):
    #     post = self.post
    #     post_list = []
    #     post_list = self.post.api_get(post.id)
    #     self.assertEquals(1, post_list.count())
