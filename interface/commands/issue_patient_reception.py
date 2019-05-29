import tkinter


from interface.common import tkinter_common


class IssuePatientReception(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)
        tkinter_common.center_window(self)
