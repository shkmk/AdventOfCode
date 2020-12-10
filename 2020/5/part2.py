def main() -> None:
    with open('in') as f:
        lines = map(str.rstrip, f.readlines())

    answer_fragments = set()
    init = False
    n_yes = 0
    for line in lines:
        if not line:
            n_yes += len(answer_fragments)
            answer_fragments.clear()
            init = False
        else:
            if init:
                answer_fragments.intersection_update(line)
            else:
                answer_fragments.update(line)
                init = True

    n_yes += len(answer_fragments)
    print(n_yes)


if __name__ == '__main__':
    main()