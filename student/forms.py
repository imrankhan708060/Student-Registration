from django import forms
from . models import Student
from django_countries.widgets import CountrySelectWidget

class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields=("First_name","Last_name","Father_name","Mother_name","Date_of_birth","Email_id","Mobile_no",
        "Admission_no","Gender","Address","courses","countries","City","slug")
        widgets = {'country': CountrySelectWidget(),
        "Date_of_birth":forms.DateInput(format=('%Y-%m-%d'), 
                               attrs={'class':'form-control datetimepicker-input','data-target': '#datetimepicker1', 
                               'placeholder':'YYYY-M-DD',"id":"datetimepicker1","type":"text"}),
        "First_name":forms.TextInput(attrs={"type":"text","class":"form-control","id":"validationServer01"}),
        "Last_name":forms.TextInput(attrs={"type":"text","class":"form-control","id":"validationServer02"}),
        "Father_name":forms.TextInput(attrs={"type":"text","class":"form-control","id":"validationServer03"}),
        "Mother_name":forms.TextInput(attrs={"type":"text","class":"form-control","id":"validationServer04"}),
        "Email_id":forms.TextInput(attrs={"type":"email","class":"form-control","id":"inlineFormInputGroupEmail","placeholder":"Email"}),
        "Mobile_no":forms.NumberInput(attrs={"type":"number","class":"form-control","id":"inlineFormInputGroupTel","placeholder":"Mob"}),
        "Admission_no":forms.NumberInput(attrs={"type":"number","class":"form-control","id":"validationServer1","placeholder":"AdmissionNo"}),
        "Gender":forms.Select(attrs={"class":"form-control","id":"validationServer2"}),
        "Address":forms.TextInput(attrs={"type":"text","class":"form-control","id":"inputAddress","placeholder":"1234 Main St"}),
        "courses":forms.Select(attrs={"class":"form-control","id":"exampleFormControlSelect2"}),
        "countries":forms.Select(attrs={"class":"form-control","id":"exampleFormControlSelect2"}),
        "City":forms.TextInput(attrs={"type":"text","class":"form-control","id":"city","placeholder":"City"}),
        "slug":forms.TextInput(attrs={"type":"text","class":"form-control","id":"slug","placeholder":"Slug"}),
        
        
        
        }
        