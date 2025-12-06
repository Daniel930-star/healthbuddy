from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def nutrition_home(request):
#     return render(request, 'nutrition/nutrition.html')
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import NutritionLog
from .forms import NutritionForm

@login_required
def nutrition_list(request):
    logs = NutritionLog.objects.filter(user=request.user).order_by('-date')

    if request.method == "POST":
        form = NutritionForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('nutrition:nutrition_list')
    else:
        form = NutritionForm()

    return render(request, 'nutrition/nutrition_list.html', {'logs': logs, 'form': form})


@login_required
def edit_nutrition(request, pk):
    log = get_object_or_404(NutritionLog, pk=pk, user=request.user)
    if request.method == 'POST':
        form = NutritionForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('nutrition:nutrition_list')
    else:
        form = NutritionForm(instance=log)

    return render(request, 'nutrition/edit_nutrition.html', {'form': form})


@login_required
def delete_nutrition(request, pk):
    log = get_object_or_404(NutritionLog, pk=pk, user=request.user)
    if request.method == 'POST':
        log.delete()
        return redirect('nutrition:nutrition_list')
    return render(request, 'nutrition/delete_nutrition.html', {'log': log})
