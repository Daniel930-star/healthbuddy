from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .forms import WorkoutForm
from django.utils.dateparse import parse_datetime

# LIST WORKOUTS
def workouts_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workouts_list.html', {'workouts': workouts})




# ADD WORKOUT
def add_workout(request):
    if request.method == 'POST':
        workout_datetime_str = request.POST.get('workout_datetime')
        workout_datetime = parse_datetime(workout_datetime_str) if workout_datetime_str else None

        Workout.objects.create(
            title=request.POST['title'],
            details=request.POST['details'],
            duration=request.POST['duration'],
            workout_datetime=workout_datetime
        )
        return redirect('workouts:workouts_list')  # namespaced redirect

    return render(request, 'workouts/edit_workout.html')  # Or a separate add_workout.html if you have one


# EDIT WORKOUT
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workouts_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/edit_workout.html', {'form': form})

# DELETE WORKOUT
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.delete()
        return redirect("workouts:workouts_list")
    return render(request, "workouts/delete_workout.html", {"workout": workout})


# WORKOUT HISTORY
def workout_history(request):
    history = Workout.objects.all().order_by('-id')
    return render(request, 'workouts/workout_history.html', {'history': history})


# UPDATE WORKOUT (alternative to edit)
def update_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        workout.title = request.POST.get(f"title_{pk}")
        workout.details = request.POST.get(f"details_{pk}")
        workout.duration = request.POST.get(f"duration_{pk}")
        workout.workout_datetime = request.POST.get(f"datetime_{pk}")
        workout.save()
    return redirect('workouts:workouts_list')
