from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

from .models import NutritionLog, NutritionGoal, ProgressPhoto
from .forms import NutritionLogForm, NutritionGoalForm, ProgressPhotoForm


@login_required
def progress_home(request):
    user = request.user

    # Logs (last 30 days)
    thirty_days_ago = timezone.now().date() - timedelta(days=30)
    logs = NutritionLog.objects.filter(user=user, date__gte=thirty_days_ago).order_by('-date')

    # Weekly total (last 7 days)
    seven_days_ago = timezone.now().date() - timedelta(days=7)
    weekly_total = (
        NutritionLog.objects.filter(user=user, date__gte=seven_days_ago)
        .aggregate(total_calories=Sum('calories'))
        .get('total_calories') or 0
    )

    # Active goal
    goal = NutritionGoal.objects.filter(user=user, active=True).first()
    goal_target = goal.daily_calorie_target if goal else None

    # Chart data (last 30 days)
    labels = []
    calories_data = []
    for i in range(30):
        day = thirty_days_ago + timedelta(days=i)
        total = (
            NutritionLog.objects.filter(user=user, date=day)
            .aggregate(total_calories=Sum('calories'))
            .get('total_calories') or 0
        )
        labels.append(day.strftime('%Y-%m-%d'))
        calories_data.append(total)

    # Progress photos (newest first)
    photos = ProgressPhoto.objects.filter(user=user).order_by('-date')

    # Forms
    log_form = NutritionLogForm()
    goal_form = NutritionGoalForm()
    photo_form = ProgressPhotoForm()

    context = {
        'logs': logs,
        'weekly_total': weekly_total,
        'goal_target': goal_target,
        'labels': labels,
        'calories_data': calories_data,
        'photos': photos,
        'log_form': log_form,
        'goal_form': goal_form,
        'photo_form': photo_form,
    }

    return render(request, 'progress/progress_home.html', context)


# --- NUTRITION LOGS ----------------------------------------------------

@login_required
def add_log(request):
    if request.method == "POST":
        form = NutritionLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.user = request.user
            log.save()
    return redirect('progress:progress_home')


@login_required
def edit_log(request, pk):
    log = get_object_or_404(NutritionLog, pk=pk, user=request.user)
    if request.method == "POST":
        form = NutritionLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('progress:progress_home')
    else:
        form = NutritionLogForm(instance=log)

    return render(request, 'progress/edit_log_page.html', {'form': form, 'log': log})


@login_required
def delete_log(request, pk):
    log = get_object_or_404(NutritionLog, pk=pk, user=request.user)
    if request.method == "POST":
        log.delete()
    return redirect('progress:progress_home')


# --- GOALS --------------------------------------------------------------

@login_required
def add_goal(request):
    if request.method == "POST":
        form = NutritionGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
    return redirect('progress:progress_home')


@login_required
def edit_goal(request, pk):
    goal = get_object_or_404(NutritionGoal, pk=pk, user=request.user)
    if request.method == "POST":
        form = NutritionGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('progress:progress_home')
    else:
        form = NutritionGoalForm(instance=goal)

    return render(request, 'progress/edit_goal_page.html', {'form': form, 'goal': goal})


@login_required
def delete_goal(request, pk):
    goal = get_object_or_404(NutritionGoal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
    return redirect('progress:progress_home')


# --- PROGRESS PHOTOS ----------------------------------------------------

@login_required
def add_photo(request):
    if request.method == "POST":
        form = ProgressPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
    return redirect('progress:progress_home')


@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(ProgressPhoto, pk=pk, user=request.user)
    if request.method == "POST":
        photo.photo.delete()  # delete file
        photo.delete()
    return redirect('progress:progress_home')
