NOP, ACC, JMP = 'nop', 'acc', 'jmp'


def main() -> None:
    data = [0, 0]
    with open('in') as f:
        op_codes = f.read().split('\n')

    OP_FUNC = {
        NOP: lambda arg: None,
        ACC: lambda arg: data.__setitem__(1, data[1] + arg),
        JMP: lambda arg: data.__setitem__(0, data[0] - 1 + arg)
    }
    visited = set()
    parse_data = lambda l: [(p := l.split())[0], int(p[1])]
    op_table = list(map(parse_data, op_codes))
    data = [0, 0]
    while data[0] not in visited:
        op = op_table[data[0]]
        visited.add(data[0])
        OP_FUNC[op[0]](op[1])
        data[0] += 1
    print(data[1])


if __name__ == '__main__':
    main()