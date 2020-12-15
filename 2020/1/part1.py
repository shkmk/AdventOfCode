from functools import reduce
from operator import mul


def main():
    print(reduce(mul, (n := set(map(int, (f := open('in')).read().split()))).intersection(2020 - i for i in n))) or f.close()


if __name__ == '__main__':
    main()