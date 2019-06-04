import tkinter

from interface.common import tkinter_common

class PatientsListView(tkinter.Toplevel):
    def __init__(self, parent, names):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, None)

        self._initialize(names)
        exit_button = tkinter.Button(self, text='OK', command=self.destroy)
        exit_button.grid(row=1, column=0, sticky='news')

        tkinter_common.center_window(self)

    def _initialize(self, names):
        lb = tkinter.Listbox(self, selectmode=tkinter.SINGLE)
        for name in names:
            lb.insert(tkinter.END, name)
        lb.grid(row=0, column=0, columnspan=1, sticky='news')
