from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *    


def fix(request):
    return render(request, 'fix.html')

def create(request):
    objs = Apply.objects.filter(user = request.user)
    if len(objs):
        return redirect('update')
    if request.method == "POST":
        apply = Apply()
        objs.q1 = request.POST['q1']
        return render(request, 'complete.html')
    else:
        # 그냥 맨 처음 들어올때
        return render(request, 'fix.html', {'q' : objs})



def update(request):

    if request.method == "POST":
        # 객체 수정한거 저장
        return render(request, 'complete.html')

    else:
        # 담아서 보여주기
        objs = Apply.objects.get(user = request.user)
        
    return render(request, 'fix.html', {"q" : objs})
