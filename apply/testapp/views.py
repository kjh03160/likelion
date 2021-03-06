from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *    
from django.contrib.auth.decorators import login_required
import datetime



@login_required
def update(request):    # 지원서 수정
    if request.method == "POST":
        now = datetime.datetime.now()
        now = now.strftime('%Y/%m/%d %H:%M:%S')
        std = datetime.datetime(2020,3,25,23,59,59)
        std = std.strftime('%Y/%m/%d %H:%M:%S')
        if now > std:
            return render(request, 'over.html')
        objs = Apply.objects.filter(user = request.user)[0]
        objs.q1 = request.POST['q1']
        objs.q2 = request.POST['q2']
        objs.q3 = request.POST['q3']
        objs.q4 = request.POST['q4']
        objs.q5 = request.POST['q5']
        objs.codecademy = request.POST['codecademy']
        objs.interview = request.POST['interview']
        objs.save()  
        return render(request, 'complete.html') 
    else:
        objs = Apply.objects.get(user = request.user)
        
    return render(request, 'fix.html', {"q" : objs})

@login_required
def create(request):    # 지원서 새로 작성
    
    objs = Apply.objects.filter(user = request.user)
    if len(objs):
        return redirect('update')
            # result = datetime.datetime.strptime(day,"%b %d, %Y %H:%M %p")
            # now = datetime.datetime.now()
    
    now = datetime.datetime.now()
    now = now.strftime('%Y/%m/%d %H:%M:%S')
    std = datetime.datetime(2020,3,26,00,00,00)
    std = std.strftime('%Y/%m/%d %H:%M:%S')
    if now > std:
        return render(request, 'over.html')
    if request.method == "POST":
        
        apply = Apply()
        apply.q1 = request.POST['q1']
        apply.q2 = request.POST['q2']
        apply.q3 = request.POST['q3']
        apply.q4 = request.POST['q4']
        apply.q5 = request.POST['q5']
        apply.codecademy = request.POST['codecademy']
        apply.interview = request.POST['interview']
        apply.user = request.user
        apply.signup = Signup.objects.get(user=request.user)
        apply.save()
        return render(request, 'complete.html') 
    else:
        # 그냥 맨 처음 들어올때
        return render(request, 'fix.html', {'q' : objs})


def view(request):  # 운영진 페이지
    if request.user.is_staff:
        posts = Apply.objects.all().order_by('-first_pf').filter(first_pf="P")
        pass_num = 0
        fail = 0
        off = 0
        for i in posts:
            if i.first_pf == "P":
                pass_num += 1
            if i.first_pf  == "F":
                fail += 1
            if i.interview == "off" and i.first_pf =="P":
                off += 1

        return render(request, 'detail.html', {'posts' : posts, 'pass' : pass_num, 'fail' : fail , 'off' : off})
    else:
        return render(request, 'alert.html')

def lookup(request, pk):    # 운영진 지원자 지원서 보기 상세 페이지
    if request.user.is_staff:

        post = get_object_or_404(Apply, pk = pk)
        return render(request, 'lookup.html', {'q' : post})
    else:
        return render(request, 'alert.html')

def assess(request, pk):    # 운영진 P/F 평가 페이지
    if request.user.is_superuser:
        post = get_object_or_404(Apply, pk = pk)
        if request.method == "POST":
            try:
                first = request.POST['first']
                post.first_pf = first
            except:
                second = request.POST['second']
                post.final_pf = second
            post.save()
            return redirect('view')
    else:
        return render(request, 'alert.html')


def user_list(request): # 지원자 현황 페이지
    if request.user.is_staff:
        users = Apply.objects.all()
        return render(request, 'users.html', {'users' : users})
    else:
        return render(request, 'alert.html')

def recruit(request):   # 모집 요강 설명 페이지
    return render(request, 'recruit.html')


def result(request):    # 지원자 결과 확인 페이지
    user1 = Apply.objects.filter(user = request.user)

    now = datetime.datetime.now()
    now = now.strftime('%Y/%m/%d %H:%M:%S')
    std = datetime.datetime(2020,4,5,12,00,00)
    std = std.strftime('%Y/%m/%d %H:%M:%S')
    if now < std and user1[0].first_pf == "P":
        return render(request, 'not.html')
    if len(user1):
        user1 = user1[0]
        print(user1.first_pf)
        return render(request, 'result.html', {'user1' : user1})

    else:
        return render (request, 'result.html', {'user1' : None})


def phone(request): # 합격자 폰 번호 보기
    objs = Apply.objects.filter(first_pf='P')
    return render(request, 'phone.html', {'phones' : objs})