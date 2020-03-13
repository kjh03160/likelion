from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *    
from django.contrib.auth.decorators import login_required

@login_required
def fix(request):
    return render(request, 'fix.html')
@login_required
def update(request):

    if request.method == "POST":
        print(12)
        objs = Apply.objects.filter(user = request.user)[0]
        objs.q1 = request.POST['q1']
        objs.q2 = request.POST['q2']
        objs.q3 = request.POST['q3']
        objs.q4 = request.POST['q4']
        objs.q5 = request.POST['q5']
        objs.codecademy = request.POST['codecademy']
        objs.save()  
        return render(request, 'complete.html') #추후에 complete로 바꿀것

    else:
        objs = Apply.objects.get(user = request.user)

        
    return render(request, 'fix.html', {"q" : objs})

@login_required
def create(request):
    objs = Apply.objects.filter(user = request.user)
    if len(objs):
        return redirect('update')
    if request.method == "POST":
        apply = Apply()
        apply.q1 = request.POST['q1']
        apply.q2 = request.POST['q2']
        apply.q3 = request.POST['q3']
        apply.q4 = request.POST['q4']
        apply.q5 = request.POST['q5']
        apply.codecademy = request.POST['codecademy']
        apply.user = request.user
        apply.signup = Signup.objects.get(user=request.user)
        apply.save()
        return render(request, 'fix.html') #추후에 complete로 바꿀것
    else:
        print(22222222222222) #test
        # 그냥 맨 처음 들어올때
        return render(request, 'fix.html', {'q' : objs})


def view(request):
    if request.user.is_staff:
        posts = Apply.objects.all()
        return render(request, 'detail.html', {'posts' : posts})
    else:
        return render(request, 'alert.html')

def lookup(request, pk):
    if request.user.is_staff:

        post = get_object_or_404(Apply, pk = pk)
        return render(request, 'lookup.html', {'q' : post})
    else:
        return render(request, 'alert.html')

def assess(request, pk):
    if request.user.is_staff:
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

