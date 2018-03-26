import unittest
import httpretty

from urllib.parse import parse_qs

from babynames.client import Client


class TestCache(dict):

    def set(self, key, value):
        self.__setitem__(key, value)

    def __bool__(self):
        return True


class TestClient(unittest.TestCase):

    CACHE = TestCache()

    def setUp(self):
        self.CACHE.clear()

    @httpretty.activate
    def test_client_requests_data(self):
        httpretty.register_uri(
            httpretty.POST,
            Client._url,
            body="<html>Baby Names</html>",
            content_type="text/html") 
        client = Client(self.CACHE)
        year = 2014
        top = 1000
        number = "n"
        client.post(year, top, number)
        req = httpretty.last_request()
        self.assertEqual(req.method, "POST")
        expected = {'number': ['n'], 'top': ['1000'], 'year': ['2014']}
        self.assertEqual(parse_qs(req.body.decode("utf-8")), expected)

    @httpretty.activate
    def test_client_requests_data_once(self):
        httpretty.register_uri(
            httpretty.POST,
            Client._url,
            body="<html>Baby Names</html>",
            content_type="text/html") 
        client = Client(self.CACHE)
        year = 2014
        top = 1000
        number = "n"
        client.post(year, top, number)
        req = httpretty.last_request()
        self.assertEqual(req.method, "POST")
        expected = {'number': ['n'], 'top': ['1000'], 'year': ['2014']}
        self.assertEqual(parse_qs(req.body.decode("utf-8")), expected)

        httpretty.reset()

        client.post(year, top, number)

        self.assertFalse(httpretty.has_request())
