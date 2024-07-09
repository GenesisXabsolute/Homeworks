calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    calls += 1
    return len(string), string.upper(), string.lower()


def is_contains(string, points):
    global calls
    calls += 1
    string1 = string.upper()
    points1 = [i.upper() for i in points]
    return string1 in points1

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

