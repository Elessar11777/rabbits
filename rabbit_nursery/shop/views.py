from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Rabbit

def list_rabbits(request):
    rabbits = Rabbit.objects.filter(available=True)
    return render(request, 'shop/rabbit_list.html', {'rabbits': rabbits})
