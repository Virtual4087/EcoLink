from django.shortcuts import render, HttpResponse
from .models import Campaign, User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def default_view(request):
    error = None
    if request.method == "POST":
        source = request.POST["form_source"]
        if source == "start_campaign":
            title = request.POST["title"]
            description = request.POST["description"]
            target = request.POST["target"]
            state = request.POST["state"]
            area = request.POST["location"]
            date = request.POST["date"]
            try:
                campaign = Campaign.objects.create(title=title, description=description, target=target, state=state, area=area, date=date)
                campaign.save()
            except Exception as e:
                error = str(e)
        elif source == "register":
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirmation = request.POST["confirmation"]
            if confirmation == password:
                try: 
                    user = User.objects.create_user(username, email, password)
                    login(request, user)
                except Exception as e:
                    error = str(e)

        elif source == "login":
            username = request.POST["username"]
            password = request.POST["password"]
            try: 
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
            except Exception as e:
                error = str(e)
    return render(request, "ecolink.html", {
        "campaigns" : Campaign.objects.all(),
        "error" : error
    })