import sys

NOP, ACC, JMP = 'nop', 'acc', 'jmp'

OP_FUNC = {
    NOP: lambda arg: None,
    ACC: lambda arg: data.__setitem__(1, data[1] + arg),
    JMP: lambda arg: data.__setitem__(0, data[0] - 1 + arg)
}

data = [0, 0]
visited = set()


def run(op_table: list[list[str, int]]) -> int:
    data[:] = [0, 0]
    visited.clear()
    while data[0] < len(op_table):
        if data[0] in visited:
            return sys.maxsize
        op = op_table[data[0]]
        visited.add(data[0])
        OP_FUNC[op[0]](op[1])
        data[0] += 1
    return data[1]


def main() -> None:
    with open('in') as f:
        op_codes = f.read().split('\n')

    parse_data = lambda l: [(p := l.split())[0], int(p[1])]
    op_table = list(map(parse_data, op_codes))
    not_acc = filter(lambda x: x[1][0] != ACC, enumerate(op_table))

    WHY = {JMP: NOP, NOP: JMP}
    for idx, inst in not_acc:
        op_table[idx][0] = WHY[inst[0]]
        if (out := run(op_table)) != sys.maxsize:
            print(out)
            break
        op_table[idx][0] = WHY[op_table[idx][0]]


if __name__ == '__main__':
    main()