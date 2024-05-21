grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_list = sorted(list(students))
my_dict = {}
middle_mark = []
for i in grades:
    middle_mark.append((sum(i) / len(i)))
for i in range(5):
    my_dict[sort_list[i]] = middle_mark[i]
print(my_dict.items())



