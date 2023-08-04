from django import forms
from .models import Details, Exhibition

class DetailsForm(forms.ModelForm):
 class Meta:
  model = Details
  fields = '__all__'
  labels = {'image':'Image'}

class ExhibitionForm(forms.ModelForm):
 class Meta:
  model = Exhibition
  fields = '__all__'
  exclude = ('user','is_verified')