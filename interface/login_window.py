import tkinter
import tkinter.messagebox


from interface.common.json_data_form import JsonDataForm
from interface.common import tkinter_common
from interface.main_menu import MainMenu


class LoginWindow(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        def do_login(data):
            if not self.controller.do_login(data['User name'], data['Password']):
                tkinter.messagebox.showerror('Error', 'Invalid user name or password')
                self.terminate()
            MainMenu(self.parent, self.controller)
            self.destroy()

        data = (
            ('User name', 'str'),
            ('Password', 'hidden_str')
        )
        JsonDataForm(self, data, 'Login', do_login, 0)

        tkinter_common.center_window(self)
