def main():
    with open('in') as f:
        jolts = [0, *set(map(int, f.read().split()))]

    diff_map = [[-1] * len(jolts) for _ in range(3)]
    jolts.append(max(jolts) + 3)
    l = len(jolts)
    d_l = l - 2

    bounds = [-1] * 6
    for s_idx, jolt in enumerate(jolts[:-1]):
        e_idx = s_idx + 1
        diff = jolts[e_idx] - jolt
        if diff == 1 and s_idx == bounds[1]:
            if bounds[3] == s_idx:
                diff_map[2][d_l - bounds[2]] = e_idx
            elif e_idx == bounds[2]:
                diff_map[2][d_l - e_idx] = bounds[3]
            diff_map[1][d_l - bounds[0]] = e_idx
            bounds[2] = bounds[0]
            bounds[3] = e_idx
        b_idx = (diff - 1) * 2
        bounds[b_idx] = s_idx
        bounds[b_idx + 1] = e_idx
        diff_map[diff - 1][d_l - s_idx] = e_idx

    n_path = [*([1] * l), 0]
    for k, paths in enumerate(zip(*diff_map)):
        n_path[d_l - k] = sum(map(n_path.__getitem__, paths))

    print(n_path[0])


if __name__ == '__main__':
    main()