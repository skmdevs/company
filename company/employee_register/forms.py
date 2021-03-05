from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('employee_fullname', 'employee_code', 'employee_mobile', 'employee_position')
        labels = {
            'employee_fullname': 'Nama Lengkap',
            'employee_code': 'NIP',
            'employee_mobile': 'Nomor Handphone',
            'employee_position': 'Posisi',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['employee_position'].empty_label = "Select"