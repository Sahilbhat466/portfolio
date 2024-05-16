from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Buy
# Create your views here.
def trends(request):
    buys = Buy.objects
    return render(request, 'buy/trends.html', {'buys':buys})

def detail(request, buy_id):
    buy_detail = get_object_or_404(Buy, pk = buy_id) # pk means primary key.(unique identifier)
    return render(request, 'buy/detail.html', {'buy':buy_detail})