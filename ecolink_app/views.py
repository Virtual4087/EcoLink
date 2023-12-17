from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Campaign, User, City
from django.contrib.auth import login, logout, authenticate
from django.core import serializers
# Create your views here.

def default_view(request):
    error = None
    if request.method == "POST":
        source = request.POST.get("form_source")
        if source == "start_campaign":
            title = request.POST.get("title")
            description = request.POST.get("description")
            target = request.POST.get("target")
            area = request.POST.get("location")
            date = request.POST.get("date")
            contact = request.POST.get("contact_no")
            chat_room = request.POST.get("chat_room")
            city = request.POST.get("city")

            try:
                campaign = Campaign.objects.create(organizer=request.user, title=title, description=description, target=target, area=area, date=date, contact_no=contact, chat_room_link=chat_room, city=City.objects.get(city=city))
                campaign.save()
                campaign.attendees.add(request.user)
                return redirect("default_view")
            except Exception as e:
                error = str(e)
        elif source == "register":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            confirmation = request.POST.get("confirmation")
            if confirmation == password:
                try: 
                    user = User.objects.create_user(username=username, email=email, password=password)
                    login(request, user)
                except Exception as e:
                    error = str(e)
            else:
                error = "Passwords don't match"
        elif source == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")
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
        "cities" : City.objects.all(),
        "error" : error
    })

def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("default_view")

def campaign(request, id):
    if request.method == "POST":
        try: 
            campaign = Campaign.objects.get(id=id)
            data = request.body.decode("utf-8")
            campaign.attendees.add(request.user)
            return JsonResponse({"success" : True})
        except:
            return JsonResponse({"success" : False})
    try:
        campaign = Campaign.objects.get(id=id)
        attendees = []
        for i in campaign.attendees.all():
            attendees.append(i.username)
        data = {
            'id' : campaign.id,
            'organizer' : campaign.organizer.username,
            'title' : campaign.title,
            'description' : campaign.description,
            'date' : campaign.date,
            'city' : campaign.city.city,
            'area' : campaign.area,
            'target' : campaign.target,
            'attendees' : attendees,
            'contact_no' : campaign.contact_no,
            'email' : campaign.organizer.email
        }
        return JsonResponse(data, safe=False)
    except Exception as e:
        return HttpResponse(str(e))