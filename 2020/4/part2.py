from itertools import starmap

VALIDATIONS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: int(x.rstrip('incm')) in {'cm': range(150, 194), 'in': range(59, 77)}.get(x[-2:], range(0,0)),
    'hcl': lambda x: len(x) == 7 and x[0] == '#' and x[1:].isalnum(),
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: len(x) == 9 and x.isdigit(),
    'cid': lambda x: True
}


def validate(s: dict[str, str]) -> bool:
    k_valid = (len(s) == 7 + ("cid" in s.keys()))
    if not k_valid:
        return False
    v_valid = all(starmap(lambda x, y: VALIDATIONS[x](y), s.items()))
    return v_valid


def main():
    with open('in') as f:
        lines = map(str.rstrip, f.readlines())
    
    s = dict()
    n_valid = 0
    for line in lines:
        if not line:
            n_valid += validate(s)
            s.clear()
        else:
            fields = line.split()
            s.update(f.split(':') for f in fields)
    n_valid += validate(s)
    print(n_valid)


if __name__ == '__main__':
    main()