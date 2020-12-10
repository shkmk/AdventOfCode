def main():
    with open('in') as f:
        lines = map(str.rstrip, f.readlines())
    
    s = set()
    n_valid = 0
    for line in lines:
        if not line:
            valid = (len(s) == 7 + ("cid" in s))
            print(s)
            n_valid += valid
            s.clear()
        else:
            fields = line.split()
            s = s.union({f[:3] for f in fields})
    print(n_valid)


if __name__ == '__main__':
    main()