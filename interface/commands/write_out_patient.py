import tkinter


from interface.common import tkinter_common
from interface.common.json_tree_view import JsonTreeView
from interface.common.data_form import DataWindow
from interface.commands.patients_selector import PatientsSelector


class WriteOutPatient:
    def __init__(self, parent, controller):
        data = (
            ('Doctor Type', 'str'),
            ('Date', 'date'),
            ('Verdict', 'str')
        )

        def callback(data):
            pass

        PatientsSelector(parent, controller, data, callback)
