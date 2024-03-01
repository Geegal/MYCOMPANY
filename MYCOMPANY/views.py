from django.shortcuts import render, redirect
from MYCOMPANY.models import Member


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'],
                        password=request.POST['password'])
        member.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'adminhome.html')
