from decimal import *


def newer_or_older_version(a: str, b: str) -> int:

    flag = 0
    if float(a) < float(b):
        flag = -1
    elif float(a) > float(b):
        flag = 1
    elif float(a) == float(b):
        if len(str(a)) > len(str(b)):
            flag = -1
        elif len(str(a)) < len(str(b)):
            flag = 1
    print(flag)
    return flag



if __name__ == '__main__':
    newer_or_older_version("1.10", "1.1")

