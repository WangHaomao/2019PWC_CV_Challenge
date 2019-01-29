import sys
from django.shortcuts import render, HttpResponse

def text(request):
    # return render(request,'pages/test.html')
    return render(request, 'pages/test.html')
def release(request):
    return render(request, 'pages/release.html')


def release_action(request):
    target_formula = request.POST.get('house_info')
    email_list = request.POST.get('house_info')
    file_name = request.POST.get('house_info')



def list(request):
    return render(request, 'pages/list.html')



