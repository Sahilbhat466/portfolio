from django.shortcuts import render
from django.http import HttpResponse 
from .models import Buy
# Create your views here.
def trends(request):
    buys = Buy.objects
    return render(request, 'buy/trends.html', {'buys':buys})