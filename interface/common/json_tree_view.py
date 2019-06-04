import tkinter
import tkinter.ttk as ttk


from interface.common import tkinter_common


width = [0, 0]


def fit(tree, item, cur=''):
    if type(item) == list:
        for i, v in enumerate(item):
            width[0] = max(width[0], len(str(i)))
            fit(tree, v, tree.insert(cur, 'end', text=str(i), open='yes'))
    elif type(item) == dict:
        for k, v in sorted(item.items()):
            width[0] = max(width[0], len(k))
            fit(tree, v, tree.insert(cur, 'end', text=k, open='yes'))
    elif type(item) == str:
        width[1] = max(width[1], len(item))
        tree.insert(cur, 'end', values=(item,))
    else:
        raise Exception('Unknown type for JSON item')


class JsonTreeView(tkinter.Toplevel):
    def __init__(self, parent, data):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, None)

        ok_button = tkinter.Button(self, text='OK', command=self.terminate)
        ok_button.grid(row=1, column=0, sticky='news')

        s = ttk.Style()
        s.configure('MyStyle.Treeview', rowheight=30)
        tree = ttk.Treeview(self, selectmode='none', columns=('Value',), show='tree', height=20, style='MyStyle.Treeview')
        fit(tree, data)
        tree.column('#0', width=width[0] * 15 + 5)
        tree.column('#1', width=width[1] * 15)
        tree.grid(row=0, column=0, sticky='news')

        tkinter_common.center_window(self)
