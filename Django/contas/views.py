from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    now = datetime.datetime.now()
    # html = f"<html><body>Agora é {now}.</body></html>"
    return render(request, "contas/home.html")