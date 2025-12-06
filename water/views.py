from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def water_home(request):
    return render(request, 'water/water.html')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from datetime import timedelta, date
from .models import WaterLog, WaterGoal
from .forms import WaterLogForm, WaterGoalForm
from django.utils import timezone

@login_required
def water_home(request):
    user = request.user
    today = timezone.now().date()

    # Logs (last 30 days)
    thirty_days_ago = today - timedelta(days=30)
    logs = WaterLog.objects.filter(user=user, date__gte=thirty_days_ago).order_by('-date')

    # Today's intake
    today_total = WaterLog.objects.filter(user=user, date=today).aggregate(
        total=Sum('amount_ml')
    )['total'] or 0

    # Active goal
    goal = WaterGoal.objects.filter(user=user, active=True).first()
    goal_target = goal.daily_target_ml if goal else None

    # Forms
    log_form = WaterLogForm()
    goal_form = WaterGoalForm(instance=goal)

    context = {
        'logs': logs,
        'today_total': today_total,
        'goal_target': goal_target,
        'log_form': log_form,
        'goal_form': goal_form,
    }
    return render(request, 'water/water_home.html', context)


@login_required
def add_log(request):
    if request.method == "POST":
        form = WaterLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
    return redirect('water:water_home')


@login_required
def edit_log(request, pk):
    log = get_object_or_404(WaterLog, pk=pk, user=request.user)
    if request.method == "POST":
        form = WaterLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('water:water_home')
    else:
        form = WaterLogForm(instance=log)
    return render(request, 'water/edit_log.html', {'form': form, 'log': log})


@login_required
def delete_log(request, pk):
    log = get_object_or_404(WaterLog, pk=pk, user=request.user)
    if request.method == "POST":
        log.delete()
    return redirect('water:water_home')


@login_required
def add_goal(request):
    if request.method == "POST":
        form = WaterGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
    return redirect('water:water_home')

def log_list(request):
    logs = WaterLog.objects.all()
    return render(request, 'water/log_list.html', {'logs': logs})