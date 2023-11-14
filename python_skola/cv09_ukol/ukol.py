import random

def rand_list(len, min, max):
    out = []
    for _ in range(len):
        out.append(random.randint(min, max))
    return out

def get_value_counts(data):
    values = {}
    ordered = {}
    for i in data:
        if i in values.keys():
            values[i] += 1
        else:
            values[i] = 1
    myKeys = list(values.keys())
    myKeys.sort()
    ordered = {i: values[i] for i in myKeys}
    return ordered

def common(data):
    values = list(data.keys())
    counts = list(data.values())
    id = counts.index(max(counts))
    return values[id]

def main():
    data = rand_list(9, 0, 10)
    print(data)
    print(common(get_value_counts(data)))

if __name__ == '__main__':
    main()