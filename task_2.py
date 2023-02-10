from typing import List, Dict, Callable

# вариант со списком

def callback(x: int) -> int:
    return x+x

def create_handlers(callback: Callable) -> List:
    handlers = [callback(i) for i in range(4)]
    return handlers

def execute_handlaers(handlers: List) -> str:
    for i in handlers:
        print(i)


# вариант со словарем

def callback(x: int) -> int:
    return x+x

def create_handlers(callback) -> Dict[int, Callable]:
    handlers = {x: callback for x in range(4)}
    return handlers

def execute_handlaers(handlers: Dict[int, Callable]) -> str:
    for key, value in handlers.items():
        print(value(key))


if __name__ == '__main__':
    execute_handlaers(create_handlers(callback))
