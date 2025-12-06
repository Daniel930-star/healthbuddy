from django import forms
from .models import WaterLog, WaterGoal

class WaterLogForm(forms.ModelForm):
    class Meta:
        model = WaterLog
        fields = ['amount_ml', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class WaterGoalForm(forms.ModelForm):
    class Meta:
        model = WaterGoal
        fields = ['daily_target_ml', 'start_date', 'end_date', 'active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
