from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = ''

    def get_videos(self, word):
        s = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                s.append(i.title)
        return s

    def add(self, *other):
        for i in other:
            if len(self.videos) == 0:
                self.videos.append(i)
            else:
                for j in self.videos:
                    if i.title != j.title:
                        self.videos.append(i)

    def register(self, nickname, password, age):
        a = User(nickname, password, age)
        if a not in self.users:
            self.users.append(a)
        else:
            print(f"Пользователь {nickname} уже существует")
        self.current_user = a

    def watch_video(self, name):
        if self.current_user == '':
            print('Войдите в аккаунт чтобы смотреть видео')
        else:
            for i in self.videos:
                if i.title == name:
                    if self.current_user.age < 18 and True == i.adult_mode:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        continue
                    else:
                        for j in range(i.time_now, i.duration + 1):
                            sleep(1)
                            print(j, end=' ')
                        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')