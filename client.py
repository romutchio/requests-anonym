import fake_useragent
import requests
import time

from stem import Signal
from stem.control import Controller


class Requester:
    def __init__(self):
        self.user_agent = fake_useragent.UserAgent()
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }

    def _reauth(self):
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)

    def get(self, url: str) -> requests.Response:
        headers = {
            'user-agent': self.user_agent.random,
        }

        self._reauth()
        return requests.get(url, headers=headers, proxies=self.proxies)

    def post(self, url: str, data, referrer_url: str) -> requests.Response:
        headers = {
            'user-agent': self.user_agent.random,
        }
        
        self._reauth()
        return requests.post(url, headers=headers, data=data, proxies=self.proxies)

    def test(self):
        for _ in range(50):
            ip = self.get('https://ident.me').text
            print(ip)
            time.sleep(1)
