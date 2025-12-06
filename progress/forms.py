from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import NutritionLog, NutritionGoal

class NutritionLogForm(forms.ModelForm):
    class Meta:
        model = NutritionLog
        fields = ['meal', 'calories', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'meal': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class NutritionGoalForm(forms.ModelForm):
    class Meta:
        model = NutritionGoal
        fields = ['daily_calorie_target', 'start_date', 'end_date', 'active']
        widgets = {
            'daily_calorie_target': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

from .models import ProgressPhoto

class ProgressPhotoForm(forms.ModelForm):
    class Meta:
        model = ProgressPhoto
        fields = ['photo', 'date', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

# progress/views.py
from .models import ProgressPhoto
from .forms import ProgressPhotoForm

@login_required
def progress_photos(request):
    user = request.user
    photos = ProgressPhoto.objects.filter(user=user)
    form = ProgressPhotoForm()

    if request.method == 'POST':
        form = ProgressPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = user
            photo.save()
            return redirect('progress:progress_photos')

    return render(request, 'progress/progress_photos.html', {'photos': photos, 'form': form})


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(ProgressPhoto, pk=pk, user=request.user)
    if request.method == 'POST':
        photo.photo.delete()  # delete file from storage
        photo.delete()
    return redirect('progress:progress_photos')

