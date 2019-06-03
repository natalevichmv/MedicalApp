from common.user_type import UserType
import json


class Controller:
    def __init__(self):
        self._patients = []
        self._passwords = {}
        self._login_to_type = {}

        with open('common/logins.db', 'r') as read_file:
            data = read_file.readlines()
            for line in data:
                user_type, login, password = tuple(line.split(';'))
                self._passwords[login] = password
                self._login_to_type[login] = UserType(int(user_type))

    def do_login(self, user_name, password):
        if not user_name in self._login_to_type:
            return False
        user_type = self._login_to_type[user_name]
        self._current_user_name = user_name
        self._current_user_type = user_type
        return True

    def get_user_name(self):
        return self._current_user_name

    def get_user_type(self):
        return self._current_user_type

    def get_fio(self):
        return self._current_user_name

    def do_register_patient(self, data):
        self._patients.append(data)
        return True
