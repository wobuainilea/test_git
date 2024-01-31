import sys

def test1(a, b):
    return a + b

def test2(a, b):
    return a - b

def test3(a, b):
    return a * b

def test4(a, b):
    if b != 0:
        return a / b
    else:
        return False


if __name__ == '__main__':
    count = 1
    while True:
        count += 1
        print('执行了一次')
        if count > 3:
            print(f'我退出了，count={count}')
            sys.exit()