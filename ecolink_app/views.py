from django.shortcuts import render, HttpResponse
from .models import Campaign

# Create your views here.

def default_view(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        target = request.POST["target"]
        location = request.POST["location"]
        date = request.POST["date"]
        campaign = Campaign.objects.create(title=title, description=description, target=target, location=location, date=date)
        campaign.save()
        campaign.attendees.add(request.user)
        return HttpResponse("ok")
    return render(request, "ecolink.html")