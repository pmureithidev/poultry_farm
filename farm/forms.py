from django import forms
from .models import Flock

class CreateFlockForm(forms.ModelForm):
    class Meta:
        model = Flock
        fields = ['name', 'flock_type', 'number_of_birds', 'breed', 'date_of_purchase', 'age', 'price', 'supplier', 'housing', 'notes', 'is_active']
