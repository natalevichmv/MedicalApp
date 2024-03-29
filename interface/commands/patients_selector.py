import tkinter


from interface.common import tkinter_common
from interface.common.json_tree_view import JsonTreeView
from interface.common.data_form import DataWindow


class PatientsSelector(tkinter.Toplevel):
    def __init__(self, parent, controller, data, action_name, callback,
                 only_present=True, show_list=None):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        self._data = data
        self._callback = callback
        self._action_name = action_name
        self._only_present = only_present
        self._show_list = show_list
        self._init_list()

        tkinter_common.center_window(self)

    def _init_list(self):
        lb = tkinter.Listbox(self, selectmode=tkinter.SINGLE)
        patients = self._show_list if self._show_list else self.controller.get_patients_list()
        for patient in patients:
            if not patient.get('Name'):
                continue
            if self._only_present and patient.get('Diseases', [{}])[-1].get('Wrote out'):
                continue
            lb.insert(tkinter.END, patient['Name'])
        lb.grid(row=1, column=0, columnspan=2, sticky='nesw')

        s_label = tkinter.Label(self, text='Search:')
        s_label.grid(row=0, column=0, sticky=tkinter.W)

        def update(s):
            while lb.size():
                lb.delete(0)
            for patient in patients:
                if not patient.get('Name'):
                    continue
                if not s in patient['Name']:
                    continue
                if self._only_present and patient.get('Diseases', [{}])[-1].get('Wrote out'):
                    continue
                lb.insert(tkinter.END, patient['Name'])

        sv = tkinter.StringVar()
        sv.trace('w', lambda name, index, mode, sv=sv: update(sv.get()))
        s_entry = tkinter.Entry(self, textvariable=sv)
        s_entry.grid(row=0, column=1, sticky=tkinter.E)

        def do_show():
            sel = lb.curselection()
            if sel and sel[0] < lb.size():
                name = lb.get(sel[0])
                for patient in patients:
                    if patient.get('Name') == name:
                        if self._data:
                            DataWindow(self.parent, self._data, self._action_name, lambda data: self._callback(patient, data))
                        JsonTreeView(self, patient)
                        return

        show_button = tkinter.Button(self, text='Show', command=do_show)
        show_button.grid(row=2, column=0, sticky='news')

        exit_button = tkinter.Button(self, text='Exit', command=self.destroy)
        exit_button.grid(row=2, column=1, sticky='news')

