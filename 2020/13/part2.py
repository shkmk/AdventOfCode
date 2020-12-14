from functools import partial, reduce
from itertools import repeat, starmap
from operator import itemgetter, mul, sub, floordiv

def main() -> None:
    with open('in') as f:
        t = tuple(map(lambda x: tuple(map(int, x)), 
                      filter(lambda x: x[1].isdigit(), 
                             enumerate(f.read().split()[1].split(',')))))
    n = tuple(map(itemgetter(1), t))
    p = reduce(mul, n)
    prt_p = tuple(starmap(floordiv, zip(repeat(p), n)))
    prt_s = tuple(zip(starmap(sub, map(reversed, t)), starmap(pow, zip(prt_p, repeat(-1), n)), prt_p))
    print(sum(map(partial(reduce, mul), prt_s)) % p)



if __name__ == '__main__':
    main()