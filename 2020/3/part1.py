TREE = '#'

def main():
    with open('in') as f:
        m = f.readlines()
    n_tree = 0
    l_row = len(m[0]) - 1
    for r in range(1, len(m)):
        n_tree += m[r][(r * 3) % l_row] == TREE
    print(n_tree)


if __name__ == '__main__':
    main()