from django.shortcuts import render
import requests
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.method == "POST":
        return render(request, "submitted.html")
    return render(request, "index.html")

def submitted(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "submitted.html")



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
