def main():
    n_correct = 0
    with open('in') as f:
        for l in f:
            raw_bounds, target, password = l.split()
            l_bound, u_bound = map(int, raw_bounds.split('-'))
            target = target.rstrip(":")
            n_correct += l_bound <= password.count(target) <= u_bound
    print(n_correct)


if __name__ == '__main__':
    main()