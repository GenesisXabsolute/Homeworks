def calculate_structure_sum(args):
    c = 0
    v = []
    for i in args:
        if isinstance(i, set):
            i = list(i)
        if isinstance(i, dict):
            for x in i.keys():
                v.append(x)
            k = []
            for j in i.keys():
                k.append(i[j])
            i = k[:] + v[:]
            v.clear()
        elif isinstance(i, int) or isinstance(i, float):
            c += i
        elif isinstance(i, str):
            c += len(i)
        if isinstance(i, tuple) or isinstance(i, list):
            c += calculate_structure_sum(i)
    return c


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))