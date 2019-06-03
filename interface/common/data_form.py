import re
import tkinter
import tkinter.messagebox


class DataForm():
    def __init__(self, parent, data, action_name, callback, start_row=0):
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
        action_button.grid(row=start_row, column=0, sticky=tkinter.W)

        exit_button = tkinter.Button(parent, text='Exit', command=parent.terminate)
        exit_button.grid(row=start_row, column=1, sticky=tkinter.E)

    @staticmethod
    def _create_widget(t, *args, **kwargs):
        if t in ['str', 'astr', 'date']:
            return tkinter.Entry(*args, **kwargs)
        if t == 'hidden_str':
            return tkinter.Entry(show='*', *args, **kwargs)
        raise Exception('Not implemented type {} in form'.format(t))

    @staticmethod
    def _get_data(w, name, t):
        if t in ['str', 'hidden_str', 'astr', 'date']:
            res = w.get()
            if t != 'astr' and not res:
                raise Exception("Field '{}' not filled".format(name))
            if t == 'date' and not re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', res):
                raise Exception("Field '{}' filled incorrectly: date should be in format DD.MM.YYYY".format(name))
            return w.get()
        raise Exception('Not implemented type {} in form'.format(t))
