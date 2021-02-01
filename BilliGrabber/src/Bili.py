import requests
from bs4 import BeautifulSoup


class Analyzer(object):
    def __init__(self, url) -> None:
        self.url = url

    def check_if_valid(self):
        """
        check if url is valid\n
        """
        url_head = 'https://www.bilibili.com/video/'
        if not self.url.startswith(url_head):
            self.url = f'{url_head}{self.url}'

        r = requests.get(self.url)
        r.raise_for_status()


if __name__ == "__main__":
    singlevid_url = "https://www.bilibili.com/video/BV1kW411q7N1"
    vidfolder_url = "https://www.bilibili.com/video/BV1AW411M"
    video_id = "BV1AW411M"
    a = Analyzer(singlevid_url)
    a.check_if_valid()