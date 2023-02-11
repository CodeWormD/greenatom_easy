from html.parser import HTMLParser
import requests
from dataclasses import dataclass
import pprint


class SetName:
    """Дексриптор данных для атрибутов класса GetHTMLText"""

    NAMES = {'__headers': dict, '__url': str}

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)
        else:
            raise ValueError('Не верный тип данных для url или headers')

    def validate(self, value):
        if type(value) == self.NAMES[self.name]:
            return True
        return False


@dataclass
class GetHTMLText:
    """Класс данных для GET запроса"""

    url: str = SetName()
    headers: dict = SetName()


class MyParser(HTMLParser):
    """Класс для подсчета тегов без атрибутов и тегов с атрибутами"""

    DICT_OF_TAGS = {}
    ALL_TEGS = 0
    ALL_TEGS_ATTR = 0

    def handle_starttag(self, tag, attrs):
        self.ALL_TEGS += 1
        if attrs:
            self.ALL_TEGS_ATTR += 1
        self.DICT_OF_TAGS.setdefault(tag, attrs)

    def count_unique_tegs(self):
        return len(self.DICT_OF_TAGS)

    def count_unique_tegs_with_attr(self):
        return len([i for i in self.DICT_OF_TAGS.keys() if not self.DICT_OF_TAGS[i]])

    def show_info(self):
        print('Кол-во тегов на странице greenatom.ru:')
        print()
        print(f'Кол-во уникальных тегов: {self.count_unique_tegs()}')
        print(f'Кол-во уникальных тегов с атрибутами: {self.count_unique_tegs_with_attr()}')
        print(f'Кол-во всех тегов: {self.ALL_TEGS}')
        print(f'Кол-во всех тегов с атрибутами: {self.ALL_TEGS_ATTR}')

        # для вывода уникальных тегов и их атрибутов
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
