from common.user_type import UserType


class Controller:
    def __init__(self):
        pass

    def do_login(self, user_name, password):
        self._user_name = user_name

        from random import randint
        self._user_type = UserType(randint(1, 3))
        self._user_type = UserType.CLERK

        return True

    def get_user_name(self):
        return self._user_name

    def get_user_type(self):
        return self._user_type

    def get_fio(self):
        return self._user_name
