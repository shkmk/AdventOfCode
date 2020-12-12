from itertools import islice
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
    occ_check = lambda i: next(filter(lambda x: x != FLOOR, i), FLOOR) == OCCUPIED

    debug = True
    debug_idx = 0

    def check(idx: int) -> bool:
        h = b[(st := idx // n_col * n_col):(et := st + n_col)]
        
        lchk = occ_check(islice(reversed(h), n_col - idx % n_col, None))
        rchk = occ_check(islice(h, idx % n_col + 1, None)) 

        v = b[(st := idx % n_col):(et := n_col * n_row):n_col]

        uchk = occ_check(islice(reversed(v), n_row - idx // n_col, None))
        dchk = occ_check(islice(v, idx // n_col + 1, None))

        fd = b[(st := (idx % n_col + idx // n_col) if idx <= (o := (idx // n_col + 1) * (n_col - 1)) else ((n_col - 1) + (idx - o) * n_col)):(et := (n_col * (n_row - 1) + 1 + idx % n_col - (n_row - 1 - idx // n_col)) if idx >= (o := (idx // n_col + 1) * (n_col - 1)) else (n_col * (n_row - 1) - (o - idx) * n_col + 1)):n_col - 1]
        if fd:
            fddchk = occ_check(islice(reversed(fd), (fdst := len(fd) - 1 - (idx // n_col - st // (n_col) - 1)), None))
            fduchk = occ_check(islice(fd, (fdst := idx // n_col - st // (n_col) + 1), None))
        else:
            fddchk = fduchk = 0

        bd = b[(st := (idx % n_col - idx // n_col) if idx >= (o := (idx // n_col) * (n_col + 1)) else ((o - idx) * n_col)):(et := (n_col * (n_row - 1) + 1 + idx % (n_col) + (n_row - 1 - idx // n_col)) if idx <= (o := (idx // n_col) * (n_col + 1)) else (n_col * n_row - (idx - o) * n_col - 1) + 1):n_col + 1]
        if bd:
            bddchk = occ_check(islice(reversed(bd), (bdst := len(bd) - 1 - (idx // n_col - st // (n_col) - 1)), None))
            bduchk = occ_check(islice(bd, (bdst := idx // n_col - st // (n_col) + 1), None))
        else:
            bddchk = bduchk = 0

        out = sum((lchk, rchk, uchk, dchk, fduchk, fddchk, bddchk, bduchk))
        return out

    print_board = lambda: print('\n'.join([''.join(b[(s := i * n_col):s + n_col]) for i in range(n_row)]), end='\n\n')
    A = {
        OCCUPIED: lambda idx: check(idx) >= 5,
        EMPTY: lambda idx: check(idx) == 0,
        FLOOR: lambda *args: False
    }

    B = {
        OCCUPIED: [OCCUPIED, EMPTY],
        EMPTY: [EMPTY, OCCUPIED],
        FLOOR: [FLOOR, FLOOR]
    }

    while True:
        n_seat = [0, ]
        n_change = sum(map(lambda p: (b.__setitem__(p[0], B[b[p[0]]][p[1]]) is None) * 0 + p[1] + (n_seat.__setitem__(0, n_seat[0] + (b[p[0]] == OCCUPIED)) is not None) * 0, zip(whitelist, tuple(map(lambda f, i: f(i), map(A.__getitem__, map(b.__getitem__, whitelist)), whitelist)))))

        if not n_change:
            break
    print(n_seat[0])


if __name__ == '__main__':
    main()