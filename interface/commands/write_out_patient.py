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
            if not 'Diseases' in patient:
                patient['Diseases'] = [{}]
            patient['Diseases'][-1]['Wrote out'] = data
            controller.update_patient(patient)

        PatientsSelector(parent, controller, data, 'Write Out Patient', callback)
