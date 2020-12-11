from collections import Counter
from itertools import starmap
from operator import sub
import heapq


def main():
    with open('in') as f:
        jolts = sorted(map(int, f.readlines()))
    print(jolts)
    diff = starmap(sub, zip(jolts[1:], jolts[:-1]))
    n_diff = Counter(diff)
    n_diff.update((3,1))
    print(n_diff[3] * n_diff[1])


if __name__ == '__main__':
    main()