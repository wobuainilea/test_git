import sys

if __name__ == '__main__':
    count = 1
    while True:
        count += 1
        print('执行了一次')
        if count > 3:
            print(f'我退出了，count={count}')
            sys.exit()