from django.http import JsonResponse
from django.shortcuts import render

from .models import History

def getHistory(request):
    histories = History.objects.all()
    data = []
    for history in histories:
        data.append({
            "id":history.id,
            "year":history.year,
            "title":history.title,
            "description":history.description,
        })
        print(data)
    return JsonResponse(data, safe=False)
