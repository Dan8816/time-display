from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    context = {
        'time' : strftime("%Y-%m-%d %H:%M", localtime())
    }
    return render(request, 'times/index.html', context) # updated this line
