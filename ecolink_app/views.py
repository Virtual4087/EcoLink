from django.shortcuts import render, HttpResponse, redirect
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
            area = request.POST["location"]
            date = request.POST["date"]
            contact = request.POST["contact_no"]
            chat_room = request.POST["chat_room"]

            try:
                campaign = Campaign.objects.create(organizer=request.user, title=title, description=description, target=target, area=area, date=date, contact_no=contact, chat_room_link=chat_room)
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
                    user = User.objects.create_user(username=username, email=email, password=password)
                    login(request, user)
                except Exception as e:
                    error = str(e)
            else:
                error = "Passwords don't match"
        elif source == "login":
            username = request.POST["username"]
            password = request.POST["password"]
            try: 
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect("default_view")
                else:
                    error = "Wrong Credentials"
            except Exception as e:
                    error = str(e)
    return render(request, "ecolink.html", {
        "campaigns" : Campaign.objects.all(),
        "error" : error
    })

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("default_view")
