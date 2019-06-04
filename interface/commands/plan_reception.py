import tkinter


from interface.commands.patients_selector import PatientsSelector


class PlanReception:
    def __init__(self, parent, controller):
        data = (
            ('Doctor Name', 'str'),
            ('Doctor Type', 'str'),
            ('Date', 'date')
        )

        def callback(patient, data):
            pass

        PatientsSelector(parent, controller, data, 'Plan Reception', callback, False)
