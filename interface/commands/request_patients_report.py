import tkinter


from interface.common import tkinter_common
from interface.common.json_tree_view import JsonTreeView
from interface.common.data_form import DataWindow
from interface.commands.patients_selector import PatientsSelector


class RequestPatientsReport(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        self._init_list()

        tkinter_common.center_window(self)

    def _init_list(self):
        lower_bound_label = tkinter.Label(self, text='First date')
        lower_bound_label.grid(row=0, column=0, columnspan=2, sticky=tkinter.W)
        lower_sv = tkinter.StringVar()
        lower_sv_entry = tkinter.Entry(self, textvariable=lower_sv)
        lower_sv_entry.grid(row=0, column=1, sticky=tkinter.E)

        upper_bound_label = tkinter.Label(self, text='Second date')
        upper_bound_label.grid(row=1, column=0, columnspan=2, sticky=tkinter.W)
        upper_sv = tkinter.StringVar()
        upper_sv_entry = tkinter.Entry(self, textvariable=upper_sv)
        upper_sv_entry.grid(row=1, column=1, sticky=tkinter.E)

        def do_search():
            def string_to_date(string):
                return tuple(string.split('.')[::-1])

            lower_bound = string_to_date(lower_sv.get())
            upper_bound = string_to_date(upper_sv.get())
            patients = []
            for patient in self.controller.get_patients_list():
                date = string_to_date(patient['Birth date'])
                if lower_bound <= date <= upper_bound:
                    patients.append(patient)
            PatientsSelector(self, self.controller, None, None, None,
                             only_present=False, show_list=patients)

        ok_button = tkinter.Button(self, text='Show', command=do_search)
        ok_button.grid(row=2, column=0, sticky='news')

        exit_button = tkinter.Button(self, text='Exit', command=self.destroy)
        exit_button.grid(row=2, column=1, sticky='news')
