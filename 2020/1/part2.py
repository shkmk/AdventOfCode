from functools import reduce
from itertools import combinations
from operator import mul


def main():
    print(reduce(mul, (x := next(filter(lambda x: 2020 - sum(x) in n, combinations((n := set(map(int, (f := open('in')).read().split()))),2))))) * (2020 - sum(x))) or f.close()


if __name__ == '__main__':
    main()