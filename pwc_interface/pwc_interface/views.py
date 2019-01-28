import sys
from django.shortcuts import render, HttpResponse

def text(request):
    return render(request,'test.html')