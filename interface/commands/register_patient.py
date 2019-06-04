import tkinter
import tkinter.messagebox


from interface.common.data_form import DataForm
from interface.common import tkinter_common


class RegisterPatient(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        def do_register_patient(data):
            try:
                self.controller.do_register_patient(data)
            except Exception as e:
                tkinter.messagebox.showerror('Error', str(e))
            else:
                tkinter.messagebox.showinfo('Info', 'Patient successfully registered')
            self.terminate()

        data = (
            ('Name', 'str'),
            ('Address', 'str'),
            ('Birth date', 'date'),
            ('Other', 'astr')
        )
        DataForm(self, data, 'Register Patient', do_register_patient)

        tkinter_common.center_window(self)

