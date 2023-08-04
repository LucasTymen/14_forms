from django import forms
# Import Patient below:
from .models import Owner, Patient

class OwnerCreateForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = ("first_name", "last_name", "phone")

# Add your class below:
class PatientCreateForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = ("pet_name", "animal_type", "breed", "age", "owner")
