def all_variants(text):
    for i in range(1, len(text) + 1):
        number1 = 0
        number2 = i
        while number2 < len(text) + 1:
            yield text[number1:number2]
            number1 += 1
            number2 += 1


a = all_variants("abc")
for i in a:
    print(i)
