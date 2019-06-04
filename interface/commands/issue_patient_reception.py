import tkinter


from interface.commands.patients_selector import PatientsSelector


class IssuePatientReception:
    def __init__(self, parent, controller):
        data = (
            ('Doctor Type', 'str'),
            ('Date', 'date'),
            ('Verdict', 'str')
        )

        def callback(patient, data):
            if not 'Diseases' in patient:
                patient['Diseases'] = [{}]
            if 'Wrote out' in patient['Diseases'][-1]:
                patient['Diseases'].append({})
            if not 'Receptions' in patient['Diseases'][-1]:
                patient['Diseases'][-1]['Receptions'] = []
            data['Doctor Name'] = controller.get_user_name()
            patient['Diseases'][-1]['Receptions'].append(data)
            controller.update_patient(patient)

        PatientsSelector(parent, controller, data, 'Issue Patient Reception', callback, False)

