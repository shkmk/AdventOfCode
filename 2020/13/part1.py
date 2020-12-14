from operator import itemgetter, mul

def main() -> None:
    with open('in') as f:
        data = f.read().split()
    s_id = int(data[0])
    t = tuple(map(int, filter(str.isdigit, data[1].split(','))))
    
    diff = min(zip(t, map(lambda x: x - s_id % x, t)), key=itemgetter(1))
    print(mul(*diff))



if __name__ == '__main__':
    main()