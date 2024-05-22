def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3, 'evfe', False)
print_params(4, 'fdvfv')
print_params(b = 25)#работает
print_params(c = [1,2,3])#работает

values_list = [1, 'spisok', True]
values_dict = {'a': 1, 'b': 'qwerty', 'c': False}
#print_params(*values_list, **values_dict) не работает
values_list_2 = [1, 'veeefe']
print_params(*values_list_2, 42)#работает

