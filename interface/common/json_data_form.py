import tkinter


class JsonDataForm():
    def __init__(self, parent, data, action_name, callback, start_row=1):
        widgets = {}
        for name, t in data:
            label = tkinter.Label(parent, text=name+':')
            label.grid(row=start_row, column=0, sticky=tkinter.W)

            widgets[name] = JsonDataForm._create_widget(t, parent)
            widgets[name].grid(row=start_row, column=1, sticky=tkinter.E)

            start_row += 1

        def command():
            res = {}
            for name, t in data:
                res[name] = JsonDataForm._get_data(widgets[name], t)
            callback(res)

        action_button = tkinter.Button(parent, text=action_name, command=command)
        action_button.grid(row=start_row, column=0, sticky=tkinter.W)

        exit_button = tkinter.Button(parent, text='Exit', command=parent.terminate)
        exit_button.grid(row=start_row, column=1, sticky=tkinter.E)

    @staticmethod
    def _create_widget(t, *args, **kwargs):
        if t == 'str':
            return tkinter.Entry(*args, **kwargs)
        if t == 'hidden_str':
            return tkinter.Entry(show='*', *args, **kwargs)
        raise Exception('Not implemented type in form')

    @staticmethod
    def _get_data(w, t):
        if t in ['str', 'hidden_str']:
            return w.get()
        raise Exception('Not implemented type in form')
