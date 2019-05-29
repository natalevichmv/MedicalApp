import tkinter
import tkinter.messagebox


from interface.common import tkinter_common
from interface.main_menu import MainMenu


class LoginWindow(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        self._add_labels()
        self._add_buttons()
        tkinter_common.center_window(self)

    def _add_labels(self):
        self.user_name_label = tkinter.Label(self, text='User name:')
        self.user_name_label.grid(row=0, column=0, sticky=tkinter.W)

        self.user_name_entry = tkinter.Entry(self)
        self.user_name_entry.grid(row=0, column=1, sticky=tkinter.E)

        self.password_label = tkinter.Label(self, text='Password:')
        self.password_label.grid(row=1, column=0, sticky=tkinter.W)

        self.password_entry = tkinter.Entry(self, show='*')
        self.password_entry.grid(row=1, column=1, sticky=tkinter.E)

    def _add_buttons(self):
        def do_login():
            user_name = self.user_name_entry.get()
            password = self.password_entry.get()
            if not self.controller.do_login(user_name, password):
                tkinter.messagebox.showerror('Error', 'Invalid user name or password')
                self.terminate()
            MainMenu(self.parent, self.controller)
            self.destroy()

        self.login_button = tkinter.Button(self, text='Login', command=do_login, width=15)
        self.login_button.grid(row=2, column=0, sticky=tkinter.W)

        self.exit_button = tkinter.Button(self, text='Exit', command=self.terminate, width=15)
        self.exit_button.grid(row=2, column=1, sticky=tkinter.E)

