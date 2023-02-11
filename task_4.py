import requests
from typing import Callable


def get_response(url: str, headers: dict) -> Callable:
    response = requests.get(url=url, headers=headers)
    return response

def get_ip(response: Callable) -> str:
    print(response.json()['ip_addr'])


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 08)'}
    url = 'https://ifconfig.me/all.json'
    get_ip(get_response(url, headers))