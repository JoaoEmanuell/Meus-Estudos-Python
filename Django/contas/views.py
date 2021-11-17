from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    data = {}

    data['days'] = [5, 6, 7, 8, 9, 10]

    data['now'] = datetime.datetime.now()
    
    return render(request, "contas/home.html", data)