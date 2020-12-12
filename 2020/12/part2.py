from collections import deque
from itertools import islice, repeat, starmap
from operator import add, mul, sub

DIR_MAP = dict(zip('ESWN', range(4)))


def main():
    w_pos = deque([10, 0, 0, 1])
    s_pos = [0] * 4

    rot = lambda a, d: w_pos.rotate(a[1] // 90 * (d * 2 - 1))

    DIR_FUNC = {
        'L': lambda a: rot(a, False),
        'R': lambda a: rot(a, True),
        'F': lambda a: any(starmap(s_pos.__setitem__, enumerate(starmap(add, zip(s_pos, starmap(mul, zip(repeat(a[1]), w_pos)))))))
    }

    std_move = lambda a: w_pos.__setitem__(DIR_MAP[a[0]], w_pos[DIR_MAP[a[0]]] + a[1])
    parse = lambda d: (d[0], int(d[1:]))

    any(map(lambda a: DIR_FUNC.get(a[0], std_move)(a), map(parse, (f := open('in')).read().split()))) or (f.close() is None)
    print(sum(map(abs, starmap(sub, map(lambda i: islice(s_pos, i, None, 2), range(2))))))


if __name__ == '__main__':
    main()