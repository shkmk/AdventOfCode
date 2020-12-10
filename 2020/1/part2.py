from functools import reduce
from operator import mul

def main():
    o = set()
    with open('main.in') as f:
        n = set(map(int, f.readlines()))
        for d in n:
            n_inv = set(2020 - (d + i) for i in n)
            f = n.intersection(n_inv)
            if not f:
                continue
            s = 2020 - sum(f)
            o.add(s)
    print(reduce(mul, o))


if __name__ == '__main__':
    main()