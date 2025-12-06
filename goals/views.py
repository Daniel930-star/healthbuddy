from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from progress.models import NutritionGoal
from .forms import NutritionGoalForm

@login_required
def goals_home(request):
    user = request.user
    goals = NutritionGoal.objects.filter(user=user).order_by('-start_date')
    active_goal = goals.filter(active=True).first()
    goal_form = NutritionGoalForm()

    context = {
        'goals': goals,
        'active_goal': active_goal,
        'goal_form': goal_form,
    }

    return render(request, 'goals/goals_home.html', context)


@login_required
def add_goal(request):
    if request.method == "POST":
        form = NutritionGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
    return redirect(reverse('goals:goals_home'))


@login_required
def edit_goal(request, pk):
    goal = get_object_or_404(NutritionGoal, pk=pk, user=request.user)
    if request.method == "POST":
        form = NutritionGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals:goals_home')
    else:
        form = NutritionGoalForm(instance=goal)

    return render(request, 'goals/edit_goal_page.html', {'form': form, 'goal': goal})


@login_required
def delete_goal(request, pk):
    goal = get_object_or_404(NutritionGoal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
    return redirect('goals:goals_home')
