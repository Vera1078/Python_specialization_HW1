# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет,
# есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его уровень
# доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа,
# вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

import json
from exceptions import *
from user import User

class Project:
    def __init__(self, users_list=None):
        if users_list is None:
            self.users_list = []
            self.ids_list = []
        else:
            self.users_list = users_list
            self.ids_list = [user.user_id for user in users_list]
        self.admin = None

    @classmethod
    def get_users_list(cls, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            users_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        users_list = []
        for level, users in users_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                users_list.append(user)
        return cls(users_list)

    def login(self, name, user_id):
        user_to_check = User(name, user_id)
        if user_to_check not in self.users_list:
            raise AccessError(user_to_check.name, user_to_check.user_id)
        for user in self.users_list:
            if user == user_to_check:
                self.admin = user
                print(f'{user_to_check}, Вы успешно вошли в систему!')
                break

    def add_user(self, name, user_id, level):
        if self.admin is None:
            raise NoAdminError
        if level < self.admin.level:
            raise LevelError(level, self.admin.level)
        if user_id in self.ids_list:
            raise DoubleIdError(user_id)
        self.users_list.append(User(name, user_id, level))
        self.ids_list.append(user_id)

    def del_user(self, name, user_id, level):
        if level < self.admin.level:
            raise LevelError
        try:
            self.users_list.remove(User(name, user_id, level))
        except ValueError:
            print('Пользователь в списке отсутствует!')

    def save_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            users_dict = {}
            for user in self.users_list:
                if user.level not in users_dict:
                    users_dict[user.level] = {user.user_id: user.name}
                else:
                    users_dict[user.level][user.user_id] = user.name
            json.dump(users_dict, file, ensure_ascii=False)


p = Project().get_users_list('users.json')
print(p.users_list)
p.login('sam', 2)
print(f'Админ: {p.admin}')
p.add_user('Fuchs', 7, 4)
p.save_file('users_pro.json')