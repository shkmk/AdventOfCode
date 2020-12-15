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
        k = [['0', s] if (s := l.rstrip(' bags')).startswith('no ') else s.split(maxsplit=1) for l in line[1].rstrip('.').split(', ')]
        kv_tbl.setdefault(v, dict())
        for c, sk in k:
            kv_tbl[v][sk] = int(c)

    why = lambda d: sum(v * (why(kv_tbl.get(k, {})) + 1) for k, v in d.items()) if d else 0

    print(why(kv_tbl['shiny gold']))

if __name__ == '__main__':
    main()