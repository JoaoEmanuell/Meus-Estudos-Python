from django.shortcuts import redirect, render
from.models import Transation
from .forms import TransationForm

# Create your views here.

def home(request):
    data = {}
    data['Transations'] = Transation.objects.all()
    
    return render(request, "contas/home.html", data)

def new_transation(request):
    data = {}
    data['form'] = TransationForm(request.POST or None)

    if data['form'].is_valid():
        data['form'].save()
        return redirect('home')

    return render(request, "contas/form.html", data)

def update(request, pk):
    transation = Transation.objects.get(pk=pk)
    form = TransationForm(request.POST or None, instance=transation)

    if form.is_valid():
        form.save()
        return redirect('home')

    data = {'form' : form, 'obj' : transation}
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transation = Transation.objects.get(pk=pk)
    transation.delete()
    return redirect('home')