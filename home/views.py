from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')
def public_home(request):
    slides = [
        "Welcome to FitLife — your all-in-one health & fitness companion designed to help you build healthy habits and stay consistent.",
        "Tracking your health matters. When you monitor your habits, you understand your progress, stay motivated, and reach your goals faster.",
        "Workouts — create routines, follow exercises, and track every rep, set, and session with ease.",
        "Nutrition — monitor your meals, balance your diet, understand macros, and stay fueled for your goals.",
        "Water Tracking — stay hydrated daily with simple logs and personalized hydration goals.",
        "Goals — set achievable targets and follow your journey step by step toward long-term success.",
        "Progress — visualize your improvements, celebrate milestones, and stay inspired every day.",
    ]

    return render(request, "home/home_public.html", {"slides": slides})

    if request.user.is_authenticated:
        return redirect("dashboard")