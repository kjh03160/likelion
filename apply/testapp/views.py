from django.shortcuts import render
from django.contrib.auth.models import User
from models import *    
def fix(request):
    return render(request, 'fix.html')

def submit(request):
    user = request.user