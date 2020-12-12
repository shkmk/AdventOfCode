from cProfile import runctx
from itertools import islice, starmap
from operator import sub
from time import perf_counter

DIR_MAP = dict(zip('ESWN', range(4)))


def main():
    data = [0] * 5

    DIR_FUNC = {
        0: (mv := lambda a, d: data.__setitem__(4, (data[4] + a[1] // 90 * (d * 2 - 1)) % 4)),
        'L': lambda a: mv(a, False),
        'R': lambda a: mv(a, True),
        'F': lambda a: data.__setitem__(data[4], data[data[4]] + a[1])
    }

    std_move = lambda a: data.__setitem__(DIR_MAP[a[0]], data[DIR_MAP[a[0]]] + a[1])
    parse = lambda d: (d[0], int(d[1:]))

    any(map(lambda a: DIR_FUNC.get(a[0], std_move)(a), map(parse, (f := open('in')).read().split()))) or (f.close() is None)
    print(sum(map(abs, starmap(sub, map(lambda i: islice(data, i, 4, 2), range(2))))))


if __name__ == '__main__':
    st = perf_counter()
    main()
    print(perf_counter() - st)