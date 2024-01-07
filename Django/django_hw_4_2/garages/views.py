from django.shortcuts import render
from .models import Garages
# Create your views here.
def index(request):
    garages = Garages.objects.all()
    context = {
        'garages' : garages
    }
    return render(request, 'index.html', context)