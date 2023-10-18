from django.shortcuts import render
from things.forms import ThingsForm

def home(request):
    form = ThingsForm()
    return render(request, 'home.html', {'form': form})
