import tkinter


from interface.commands.patients_selector import PatientsSelector


class RequestDiseasesReport:
    def __init__(self, parent, controller):
        PatientsSelector(parent, controller, None, None, None, only_present=False)
