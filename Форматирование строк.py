team1_num = 5
print('В команде Мастера кода участников: %s !' % team1_num)

team1_num2 = 6
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team1_num2))

score_2 = 42
print("Команда Волшебники данныхрешила задач: {}".format(score_2))

team1_time = 18015.2
print("Волшебники данных решили задачи за {}".format(team1_time))

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задачи')

team2_time = 1930.5
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных'
else:
    result = 'Ничья!'

print(f'Результат битвы: Победа команды Мастер кода ')

task_total = score_1 + score_2
time_avg = 455
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} задач в секунду')