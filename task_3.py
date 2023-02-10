from html.parser import HTMLParser
import requests
from dataclasses import dataclass
import pprint


class SetName:
    """Дексриптор данных для атрибутов класса GetHTMLText"""
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) in (dict, str):
            setattr(instance, self.name, value)


@dataclass
class GetHTMLText:
    """Класс данных для GET запроса"""
    url: str = SetName()
    headers: dict = SetName()


class MyParser(HTMLParser):
    """Класс для подсчета тегов и их атрибутов"""

    DICT_OF_TAGS = {}

    def handle_starttag(self, tag, attrs):
        self.DICT_OF_TAGS.setdefault(tag, attrs)

    def show_info(self):
        tegs = len(self.DICT_OF_TAGS)
        tegswithattr = len([i for i in self.DICT_OF_TAGS.keys() if not self.DICT_OF_TAGS[i]])
        print(f'Кол-во тегов: {tegs}')
        print(f'Кол-во тегов с атрибутами: {tegswithattr}')

        # для вывода тегов и их атрибуты
        #pprint.pprint(self.DICT_OF_TAGS)


if __name__ == '__main__':
    # формируем класс данных для запроса
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 08)'}
    url = 'https://greenatom.ru'
    data = GetHTMLText(url=url, headers=headers)

    # отправляем запрос
    response = requests.get(url=data.url, headers=data.headers)

    # парсим данные
    parser = MyParser()
    parser.feed(response.text)
    parser.show_info()
