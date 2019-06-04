import re
import tkinter
import tkinter.messagebox


from interface.common import tkinter_common


class DataForm():
    def __init__(self, parent, data, action_name, callback, start_row=0, term=False):
        widgets = {}
        for name, t in data:
            label = tkinter.Label(parent, text=name+':')
            label.grid(row=start_row, column=0, sticky=tkinter.W)

            widgets[name] = DataForm._create_widget(t, parent)
            widgets[name].grid(row=start_row, column=1, sticky=tkinter.E)

            start_row += 1

        def command():
            res = {}
            for name, t in data:
                try:
                    res[name] = DataForm._get_data(widgets[name], name, t)
                except Exception as e:
                    tkinter.messagebox.showerror('Error', str(e))
                    return
            callback(res)

        action_button = tkinter.Button(parent, text=action_name, command=command)
        action_button.grid(row=start_row, column=0, sticky='news')

        exit_button = tkinter.Button(parent, text='Exit', command=(parent.terminate if term else parent.destroy))
        exit_button.grid(row=start_row, column=1, sticky='news')

    @staticmethod
    def _create_widget(t, *args, **kwargs):
        if t in ['str', 'astr', 'date', 'phone', 'blood']:
            return tkinter.Entry(*args, **kwargs)
        if t == 'hidden_str':
            return tkinter.Entry(show='*', *args, **kwargs)
        raise Exception('Not implemented type {} in form'.format(t))

    @staticmethod
    def _get_data(w, name, t):
        if t in ['str', 'hidden_str', 'astr', 'date', 'phone', 'blood']:
            res = w.get()
            if t != 'astr' and not res:
                raise Exception("Field '{}' not filled".format(name))
            if t == 'date' and not re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', res):
                raise Exception("Field '{}' filled incorrectly: date should be in format DD.MM.YYYY".format(name))
            if t == 'blood' and not res in ('1', '2', '3', '4', 'I', 'II', 'III', 'IV', '0', 'A', 'B', 'AB'):
                raise Exception('Invalid blood group')
            if t == 'phone' and not re.fullmatch(r'\+?[0-9\-()]+', res):
                raise Exception('Invalid phone format')
            return w.get()
        raise Exception('Not implemented type {} in form'.format(t))


class DataWindow(tkinter.Toplevel):
    def __init__(self, parent, data, action_name, callback, start_row=0):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, None)

        def new_callback(data):
            callback(data)
            self.destroy()

        DataForm(self, data, action_name, new_callback, start_row)

        tkinter_common.center_window(self)
