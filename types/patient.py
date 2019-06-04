class Patient():
    def __init__(self, name, info):
        self._name = name
        self._info = info

    def get_name(self):
        return self._name

    def get_info(self):
        return self._info
