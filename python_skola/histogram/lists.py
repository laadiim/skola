import random

def rand_list(len, min, max):
    out = []
    for _ in range(len):
        out.append(random.randint(min, max))
    return out

def get_value_counts(data):
    values = {}
    for i in data:
        if str(i) in values.keys():
            values[str(i)] += 1
        else:
            values[str(i)] = 1
    return values

def main():
    data = rand_list(10, -5, 5)
    print(data)
    print(get_value_counts(data))