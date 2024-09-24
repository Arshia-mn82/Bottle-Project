from django.shortcuts import render
from .models import Ranking

def ranking_view(request):
    rankings = Ranking.objects.order_by('-bottles_read')
    return render(request, "rankings_app/ranking.html", {"rankings": rankings})