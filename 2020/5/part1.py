def main() -> None:
    with open('in') as f:
        lines = map(str.rstrip, f.readlines())

    answer_fragments = set()
    n_yes = 0
    for line in lines:
        if not line:
            n_yes += len(answer_fragments)
            answer_fragments.clear()
        else:
            answer_fragments.update(line)
    n_yes += len(answer_fragments)
    print(n_yes)


if __name__ == '__main__':
    main()