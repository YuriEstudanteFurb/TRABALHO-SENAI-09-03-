from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def paris(request):
    return render(request, 'paris.html')

def oquefazer(request):
    return render(request, 'oquefazer.html')

