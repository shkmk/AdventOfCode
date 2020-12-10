def main():
    n_correct = 0
    with open('in') as f:
        for l in f:
            raw_indices, target, password = l.split()
            indices = map(lambda x: int(x) - 1, raw_indices.split('-'))
            target = target.rstrip(":")
            matches = set(map(password.__getitem__, indices))
            n_correct += (len(matches) != 1 and target in matches)

    print(n_correct)


if __name__ == '__main__':
    main()