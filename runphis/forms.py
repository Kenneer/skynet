from django import forms
from .models import perfilnk
class perfilform(forms.ModelForm):
	class Meta:
		model = perfilnk
		fields = ['nombre', 'apellidos','movil','email']
		widgets ={
		  'nombre':forms.TextInput(attrs={'class': 'form-control'}),
		  'apellidos':forms.TextInput(attrs={'class': 'form-control'}),
		  'movil':forms.TextInput(attrs={'class': 'form-control'}),
		  'email':forms.TextInput(attrs={'class': 'form-control'})
	    
		  
		  
		}
