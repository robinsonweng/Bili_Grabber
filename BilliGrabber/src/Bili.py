import requests
from bs4 import BeautifulSoup


class Analyzer(object):
    def __init__(self, url) -> None:
        self.url = url

    def check_if_valid(self):
        r = requests.get(self.url)
        print(r)
        print(r.text)