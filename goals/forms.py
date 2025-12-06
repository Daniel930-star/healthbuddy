# goals/forms.py
from django import forms
from progress.models import NutritionGoal

class NutritionGoalForm(forms.ModelForm):
    class Meta:
        model = NutritionGoal
        fields = ['daily_calorie_target', 'start_date', 'end_date', 'active']
        widgets = {
            'daily_calorie_target': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
