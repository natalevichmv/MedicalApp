from common.user_type import UserType
import json


class Controller:
    def __init__(self):
        self._patients = []
        self._passwords = {}
        self._login_to_type = {}
        self._load_logins()
        self._load_patients()

    def _load_patients(self):
        try:
            with open('common/patients.db', 'r') as p_file:
                self._patients = json.load(p_file)
        except:
            pass

    def _save_patients(self):
        with open('common/patients.db', 'w') as p_file:
            json.dump(self._patients, p_file)

    def _load_logins(self):
        with open('common/logins.db', 'r') as read_file:
            data = read_file.readlines()
            for line in data:
                user_type, login, password = (x.strip() for x in line.split(';'))
                self._passwords[login] = password
                self._login_to_type[login] = UserType(int(user_type))

    def do_login(self, user_name, password):
        if not user_name in self._login_to_type:
            return False
        if self._passwords[user_name] != password:
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
        for patient in self._patients:
            if data['Name'] == patient['Name']:
                raise Exception('Patient is already registered')
        self._patients.append(data)
        self._save_patients()
        return True

    def get_patients_list(self):
        return self._patients

    def update_patient(data):
        for i, patient in enumerate(self._patients):
            if patient['Name'] == name['Name']:
                self._patients[i] = data
                self._save_patients()
                return True
        return False
