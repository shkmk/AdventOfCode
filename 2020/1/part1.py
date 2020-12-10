from functools import reduce
from operator import mul

def main():
    with open('in') as f:
        n = set(map(int, f.readlines()))
        n_inv = set(2020 - i for i in n)
    print(reduce(mul, n.intersection(n_inv)))

if __name__ == '__main__':
    main()