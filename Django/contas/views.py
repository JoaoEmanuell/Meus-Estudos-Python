from django.shortcuts import render
from.models import Transation
# Create your views here.

def home(request):
    data = {}
    data['Transations'] = Transation.objects.all()
    
    return render(request, "contas/home.html", data)