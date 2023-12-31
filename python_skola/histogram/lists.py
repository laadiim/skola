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

def hist(data):
    labels = data.keys()
    buffer = '_|'
    for i in labels:
        if int(i) >= 0:
            print(f'  {i}|| {data[i]*buffer}')
        else:
            print(f' {i}|| {data[i]*buffer}')
    

def main():
    data = rand_list(10, -5, 5)
    print(data)
    print(get_value_counts(data))
    hist(get_value_counts(data))

if __name__ == '__main__':
    main()