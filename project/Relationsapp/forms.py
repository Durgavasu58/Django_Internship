
from django import forms
from .models import Studentdata, Lecturer, Departmentbranch

class StudentForm(forms.ModelForm):
	class Meta:
		model = Studentdata
		fields = "__all__"

class LecturerForm(forms.ModelForm):
	class Meta:
		model = Lecturer
		fields = "__all__"
	
class DepartForm(forms.ModelForm):
	class Meta:
		model = Departmentbranch
		fields = "__all__"