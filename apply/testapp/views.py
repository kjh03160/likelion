from django.shortcuts import render

def fix(request):
    return render(request, 'fix.html')

def submit(request):