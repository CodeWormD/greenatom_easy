from typing import List, Dict, Callable

# вариант со списком

def callback(x: int) -> int:
    """Функция для наглядности"""
    return x+x

def create_handlers(callback: Callable) -> List[Callable[[int]]]:
    handlers: List = [callback(i) for i in range(4)]
    return handlers

def execute_handlaers(handlers: List) -> str:
    for i in handlers:
        return i


# вариант со словарем

def callback2(x: int) -> int:
    """Функция для наглядности"""
    return x+x

def create_handlers2(callback: Callable) -> Dict[int, Callable]:
    handlers: dict = {x: callback for x in range(4)}
    return handlers

def execute_handlaers2(handlers: Dict[int, Callable]) -> str:
    for key, value in handlers.items():
        return value(key)


if __name__ == '__main__':
    execute_handlaers(create_handlers(callback))
    execute_handlaers2(create_handlers2(callback2))
