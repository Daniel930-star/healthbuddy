from django import forms
from .models import NutritionLog

class NutritionForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['meal_type', 'food_name', 'calories', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
