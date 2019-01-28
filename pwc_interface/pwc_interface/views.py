import sys
from django.shortcuts import render, HttpResponse

def text(request):
    # return render(request,'pages/test.html')
    return render(request, 'pages/test.html')
def release(request):
    return render(request, 'pages/release.html')
def list(request):
    return render(request, 'pages/list.html')
