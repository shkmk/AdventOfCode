from itertools import chain
from operator import itemgetter

FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'


def main():
    with open('in') as f:
        b = f.read().split()

    n_col = len(b[0])
    n_row = len(b)
    b = list(''.join(b))
    ignore = set(
        map(itemgetter(0), filter(lambda x: x[1] == FLOOR, enumerate(b))))
    whitelist = set(range(n_col * n_row)).difference(ignore)

    debug = False
    check = lambda b, idx: (s := sum(
            map(
                lambda x: x == OCCUPIED,
                chain(
                    b[(st := max(st_idx := idx - n_col - 1, l_bound := (st_idx + 1) // n_col * n_col)):(et := max(0, min(st_idx + 3, l_bound + n_col)))], 
                    [(l_bound := idx // n_col * n_col) * 0, (u_bound := l_bound + n_col) * 0],
                    b[(st := max(l_bound + (idx - 1 < l_bound), idx - 1)):(et := min(u_bound, idx + 3)):2],
                    b[(st := max(st_idx := idx + n_col - 1, l_bound := (st_idx + 1) // n_col * n_col)):(et := min(n_row * n_col, min(st_idx + 3, l_bound + n_col)))]
                )
            )
        )
    ) + ((print(f'{idx}: {s}, [{st}:{et}] {b[st:et]}') if debug and idx >= 0 else None) is not None)

    print_board = lambda: print('\n'.join([''.join(b[(s := i * n_col):s + n_col]) for i in range(n_row)]))
    A = {
        OCCUPIED: lambda b, idx: check(b, idx) >= 4,
        EMPTY: lambda b, idx: check(b, idx) == 0,
        FLOOR: lambda *args: False
    }

    B = {
        OCCUPIED: [OCCUPIED, EMPTY],
        EMPTY: [EMPTY, OCCUPIED],
        FLOOR: [FLOOR, FLOOR]
    }

    while True:
        n_seat = [0, ]
        n_change = sum(map(lambda p: (b.__setitem__(p[0], B[b[p[0]]][p[1]]) is None) * 0 + p[1] + (n_seat.__setitem__(0, n_seat[0] + (b[p[0]] == OCCUPIED)) is not None) * 0, zip(whitelist, tuple(map(lambda f, i: f(b, i), map(A.__getitem__, map(b.__getitem__, whitelist)), whitelist)))))
        if not n_change:
            break
    print(n_seat[0])


if __name__ == '__main__':
    main()