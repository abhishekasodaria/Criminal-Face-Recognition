from django import forms
from .models import criminaldata,Image

class multi(forms.ModelForm):
	Name = forms.CharField(max_length = 255)
	FathersName = forms.CharField(max_length = 255,required = False)
	MothersName = forms.CharField(max_length = 255,required = False)
	Gender = forms.CharField(max_length = 255,required = False)
	DOB = forms.CharField(max_length = 255,required = False)
	BloodGroup = forms.CharField(max_length = 255,required = False)
	IdentificationMark = forms.CharField(max_length = 255,required = False)
	Nationality = forms.CharField(max_length = 255,required = False)
	Religion = forms.CharField(max_length = 255,required = False)
	CrimesDone = forms.CharField(max_length = 255,required = False)
	ImageField = forms.ImageField(widget = forms.ClearableFileInput(attrs = {"multiple":True}))
	
	class Meta:
		model = criminaldata
		fields = ('Name','FathersName','MothersName','Gender','DOB','BloodGroup','IdentificationMark','Nationality','Religion','CrimesDone')

class ImageForm(forms.ModelForm):
	Image = forms.ImageField(label = 'Image')
	class Meta:

		model = Image
		fields = ('Image',)