import tkinter


from common.user_type import UserType
from interface.common import tkinter_common

from interface.commands.register_patient import RegisterPatient
from interface.commands.register_treatment_course import RegisterTreatmentCourse
from interface.commands.request_patients_report import RequestPatientsReport
from interface.commands.request_diseases_report import RequestDiseasesReport
from interface.commands.plan_reception import PlanReception
from interface.commands.issue_patient_reception import IssuePatientReception
from interface.commands.write_out_patient import WriteOutPatient
from interface.commands.request_disease_history import RequestDiseaseHistory
from interface.commands.prescribe_treatment import PrescribeTreatment


class MainMenu(tkinter.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tkinter_common.default_init(self, parent, controller)

        self._add_labels()
        self._add_buttons()
        tkinter_common.center_window(self)

    def _add_labels(self):
        hello_label = tkinter.Label(self, text='Hello, {}! Choose your option as a {}'.format(
                self.controller.get_fio(),
                self.controller.get_user_type().name.title()))
        hello_label.grid(row=0, column=0)

    def _add_buttons(self):
        def add_buttons(infos):
            i = 1
            for name, cls in infos:
                def do_command(cls=cls):
                    cls(self, self.controller)
                button = tkinter.Button(self, text=name, width=70, height=2, command=do_command)
                button.grid(row=i, column=0, sticky = tkinter.W)
                i += 1

            exit_button = tkinter.Button(self, text='Exit', width=70, height=2, command=self.terminate)
            exit_button.grid(row=i, column=0, sticky=tkinter.SW)

        def add_clerk_buttons():
            add_buttons((
                ('Register Patient', RegisterPatient),
                #('Register Treatment Course', RegisterTreatmentCourse)
            ))

        def add_authority_buttons():
            add_buttons((
                ('Request Patients Report', RequestPatientsReport),
                ('Request Diseases Report', RequestDiseasesReport)
            ))

        def add_doctor_buttons():
            add_buttons((
                ('Plan Reception', PlanReception),
                ('Issue Patient Reception', IssuePatientReception),
                ('Write Out Patient', WriteOutPatient),
                ('Request Disease History', RequestDiseaseHistory),
                ('Prescribe Treatment', PrescribeTreatment)
            ))

        {
            UserType.DOCTOR: add_doctor_buttons,
            UserType.AUTHORITY: add_authority_buttons,
            UserType.CLERK: add_clerk_buttons
        }[self.controller.get_user_type()]()
