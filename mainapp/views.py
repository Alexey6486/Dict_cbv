from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainapp/index.html')
