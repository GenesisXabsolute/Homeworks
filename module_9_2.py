first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(i) for i in first_strings if len(i) >= 5]
second_result = [(i, x) for i in first_strings for x in second_strings if len(i) == len(x)]
third_result = {i: len(i) for i in first_strings + second_strings}
print(first_result)
print(second_result)
print(third_result)