from functools import partial
from itertools import chain
from string import digits

IGNORE = digits + ' '


def main() -> None:
    with open('in') as f:
        lines = [l.split(' contain ') for l in f.read().split('\n')]

    kv_tbl = {}
    for line in lines:
        v = line[0].rstrip(' bags')
        k = [l.lstrip(IGNORE).rstrip(' bags') for l in line[1].rstrip('.').split(', ')]
        for sk in k:
            kv_tbl.setdefault(sk, set())
            kv_tbl[sk].add(v)

    k = kv_tbl['shiny gold']
    c = len(k)
    while True:
        k = k.union(chain.from_iterable(filter(None, map(kv_tbl.get, k))))
        if c == len(k):
            break
        c = len(k)
    print(c)


if __name__ == '__main__':
    main()