import tkinter


from interface.commands.patients_selector import PatientsSelector


class WriteOutPatient:
    def __init__(self, parent, controller):
        data = (
            ('Doctor Type', 'str'),
            ('Date', 'date'),
            ('Verdict', 'str')
        )

        def callback(patient, data):
            pass

        PatientsSelector(parent, controller, data, 'Write Out Patient', callback)
