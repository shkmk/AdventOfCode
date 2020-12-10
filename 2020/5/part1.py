from functools import lru_cache
from math import floor
from statistics import mean


@lru_cache(maxsize=2**7)
def get_row(prtn_str: str) -> int:
    bounds = [0, 127]
    for code in prtn_str[:-1]:
        m = floor(mean(bounds))
        if code == 'B':
            bounds[0] = m + 1
        else:
            bounds[1] = m
    return (min if prtn_str[-1] == 'F' else max)(bounds)


@lru_cache(maxsize=2**3)
def get_col(prtn_str: str) -> int:
    bounds = [0, 7]
    for code in prtn_str[:-1]:
        m = floor(mean(bounds))
        if code == 'R':
            bounds[0] = m + 1
        else:
            bounds[1] = m
    return (min if prtn_str[-1] == 'L' else max)(bounds)


def main() -> None:
    with open('in') as f:
        print(
            max(
                get_row(prtn_str[:7]) * 8 + get_col(prtn_str[7:])
                for prtn_str in f))


if __name__ == '__main__':
    main()