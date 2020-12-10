from functools import reduce
from operator import mul

TRAVERSAL = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

TREE = "#"


def n_tree(m: list[str], t: list[int]) -> int:
    n_tree = 0
    l_row = len(m[0]) - 1
    for r in range(1, len(m) // t[1]):
        n_tree += m[r * t[1]][(r * t[0]) % l_row] == TREE
    return n_tree


def main() -> None:
    with open('in') as f:
        m = f.readlines()

    print(reduce(mul, (n_tree(m, t) for t in TRAVERSAL)))


if __name__ == '__main__':
    main()
