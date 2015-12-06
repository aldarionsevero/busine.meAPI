from django.test import TestCase
from django.test import Client
from ..models import Busline
from ..models import Terminal
from ..models import Post
from authentication.models import BusinemeUser

STATUS_OK = 200
STATUS_NOT_FOUND = 404
GENERIC_NOT_FOUND_ID = 99999999


class TestSearchResultView(TestCase):

    """
    This test method is used for make the tests in changes on the search
    view results.
    """

    def setUp(self):
        self.client = Client()

        self.busline = Busline()

        self.busline.line_number = '001'
        self.busline.description = 'route'
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.terminal = Terminal(description="terminal")
        self.terminal.save()
        self.busline.save()
        self.busline.terminals.add(self.terminal)

    """
    This test method is used for analysis of method obtain the corrects
    results.
    """

    def test_get(self):
        response = self.client.get("/buslines/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    """
    This test method is used for analysis of method obtain the corrects
    buslines.
    """

    def test_get_busline(self):
        bus = Busline.objects.get(description="route")
        response = self.client.get(
            "/buslines/" + str(bus.id) + "/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    """
    This test method is used for analysis of method obtain the correct
    message when the bus line is not found.
    """

    def test_get_busline_not_found(self):
        response = self.client.get(
            "/buslines/" + str(GENERIC_NOT_FOUND_ID) + "/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)


class TestTerminalSearchResultView(TestCase):

    """
    This test method is used for make the tests in changes on the terminals
    search view results.
    """

    def setUp(self):
        self.terminal = Terminal()

        self.terminal.description = "Terminal Description Test String"
        self.terminal.addres = "Terminal Adress Test String "
        self.terminal.save()

    """
    This test method is used for analysis of method obtain the corrects
    terminals.
    """

    def test_get(self):
        response = self.client.get("/terminals/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    def test_get_terminal(self):
        terminal = self.terminal.id
        response = self.client.get("/terminals/%s/" % str(terminal))
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    """
    This test method is used for analysis of method obtain the correct
    message when the terminal is not found.
    """

    def test_get_terminal_not_found(self):
        response = self.client.get(
            "/terminals/" + str(GENERIC_NOT_FOUND_ID) + "/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)


class TestPostView(TestCase):

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

    def test_get(self):
        response = self.client.get("/posts/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    def test_get_post(self):
        post_id = self.post.id
        response = self.client.get("/posts/%s/" % str(post_id))
        code = response.status_code
        self.assertEquals(code, STATUS_OK)

    def test_get_post_null(self):
        response = self.client.get('\
            /posts/%s/' % (str(GENERIC_NOT_FOUND_ID)))
        code = response.status_code
        self.assertEquals(code, STATUS_NOT_FOUND)

    def test_get_post_not_found(self):
        response = self.client.get(
            "/posts/" + str(GENERIC_NOT_FOUND_ID) + "/")
        code = response.status_code
        self.assertEquals(code, STATUS_OK)


class TestFavoriteView(TestCase):

    """docstring for TestFavoriteView"""

    def setUp(self):
        # self.favorite = Favorite()

        self.busline = Busline()
        self.busline.line_number = "002"
        self.busline.route_size = 0.1
        self.busline.fee = 3.50
        self.busline.save()

        self.user = BusinemeUser()
        self.user.username = "TestUser1"
        self.user.save()

        # self.favorite.user = self.user
        # self.favorite.busline = self.busline
        # self.favorite.save()

    def test_get_favorite_add(self):
        self.toggle_favorite(self.user.username, self.busline.line_number)

    def test_get_favorite_un_favorite(self):
        self.toggle_favorite(self.user.username, self.busline.line_number)
        # second access to un-favorite
        self.toggle_favorite(self.user.username, self.busline.line_number)

    def toggle_favorite(self, username, line_number):
        response = self.client.get(
            "/favorite/?username=" + username +
            "&line_number=" + line_number)
        code = response.status_code
        self.assertEquals(code, STATUS_OK)
