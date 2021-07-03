from .models import Postcard
from django.shortcuts import render


def index(request):
    postcards = Postcard.objects.all()
    total_distance = 0
    total_days = 0
    for postcard in postcards:
        distance = int(postcard.distance.replace(',', ''))
        days = int(postcard.time_travel)
        total_distance += distance
        total_days += days
        setattr(postcard, 'avg', distance / days)

    context = {"postcards": postcards, "total_distance": total_distance, "total_days": total_days}

    return render(request, 'index.html', context)
