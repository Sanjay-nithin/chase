from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Team
import json

# Create your views here.
def redirect_to_login(request):
    return redirect("login_team")

def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "firstpage.html")

def play(request):
    return render(request, "gamepage.html")

def open_level(request, level):
    return render(request, f'level{level}.html')

def done(request):
    return render(request, "price.html")

def question_page(request, level, question):
    total = 4

    qlinks = [{"number":i, 'url':f'level/{level}/question/{i}'} for i in range(1, total+1)]

    return render(request, f'level_{level}/question{question}.html', {
        'level': level,
        'question': question,
        'qlinks': qlinks,
    })

@csrf_exempt
def track_tab_switch(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON data
            team_name = data.get("team_name")

            if not team_name:
                return JsonResponse({"error": "Team name is required"}, status=400)

            # Process the request (e.g., log team activity)
            print(f"Tab switch detected for team: {team_name}")

            return JsonResponse({"message": "Tab switch recorded"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_tab_switch_count(request, team_name):
    try:
        team = Team.objects.get(name=team_name)
        return JsonResponse({"tabs_switched": team.tabs_switched})
    except Team.DoesNotExist:
        return JsonResponse({"tabs_switched": 0})  # Default to 0 if the team is new


def open_morse(request, level):
    return render(request, f"morse-code{level}.html")

@csrf_exempt
def register_team(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_name = data.get("team_name")

        if Team.objects.filter(name=team_name).exists():
            return JsonResponse({"success": False, "message": "Team name already exists!"})
        
        Team.objects.create(name=team_name)
        return JsonResponse({"success": True, "message": "Team registered successfully! Please login."})

@csrf_exempt
def login_team(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            team_name = data.get("team_name", "").strip()

            if not team_name:
                return JsonResponse({"success": False, "message": "Enter a valid team name."})

            if Team.objects.filter(name=team_name).exists():
                return JsonResponse({"success": True, "message": "Login successful!"})
            else:
                return JsonResponse({"success": False, "message": "Team not found. Please register."})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid request format."})

    # **Render the login page when accessed via GET**
    return render(request, "login.html")

def get_team_name(request):
    if request.user.is_authenticated:
        return JsonResponse({"team_name": request.user.team_name})  # Adjust based on your model
    return JsonResponse({"error": "User not authenticated"}, status=401)

def decypher(request):
    return render(request, "morse_code.html")