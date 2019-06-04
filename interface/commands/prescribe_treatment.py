import tkinter


from interface.commands.patients_selector import PatientsSelector


class PrescribeTreatment:
    def __init__(self, parent, controller):
        data = (
            ('Pill', 'str'),
            ('Amount', 'str'),
            ('Frequency', 'str')
        )

        def callback(patient, data):
            if not 'Diseases' in patient:
                patient['Diseases'] = [{}]
            if not 'Treatments' in patient['Diseases'][-1]:
            	patient['Diseases'][-1]['Treatments'] = []
            patient['Diseases'][-1]['Treatments'].append(data)
            controller.update_patient(patient)

        PatientsSelector(parent, controller, data, 'Prescribe treatment', callback)
