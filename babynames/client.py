from http.client import HTTPConnection
from urllib.parse import urlencode, urlparse, quote_plus
from collections import OrderedDict
from os.path import realpath, exists
from tempfile import gettempdir


class Client(object):

    _headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/html"
    } 

    _url = "http://www.socialsecurity.gov/cgi-bin/popularnames.cgi"

    def __init__(self, cache=None):
        if not cache:
            cachedir = gettempdir()
            if not cachedir:
                cachedir = "."
            self._cache = Cache(cachedir)
        else:
            self._cache = cache

    def post(self, year, top, number):
        cache_key = self._build_key(year=year, top=top, number=number)
        data = self._cache.get(cache_key)
        if not data:
            params = urlencode({"year":year, "top":top, "number":number})
            self._connection.request("POST", self._url_parts[1], params, self._headers)
            response = self._connection.getresponse()
            data = response.readall().decode("utf-8")
            self._cache.set(cache_key, data)
            self._connection.close()
        return data

    def _build_key(self, year, top, number):
        compound = "year{}top{}number{}".format(year, top, number)
        return quote_plus(self._url) + "".join(compound)

    @property
    def _url_parts(self):
        parts = urlparse(self._url)
        return (parts.netloc, parts.path)
        
    @property
    def _connection(self):
        try:
            self._c
        except AttributeError:
            self._c = HTTPConnection(self._url_parts[0])
        return self._c


class Cache(object):

    def __init__(self, cache_path):
        self._cache_path = cache_path

    def get(self, key):
        path = self._key_path(key)
        result = None
        if exists(path):
            with(open(path)) as f:
                result = f.read()
        return result

    def set(self, key, data):
        with(open(self._key_path(key), "w+")) as f:
            f.write(data)

    def _key_path(self, key):
        return realpath("/".join((self._cache_path, key)))
