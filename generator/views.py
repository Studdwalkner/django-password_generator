from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'password':'gdadgajjdjkad'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('Specail'):
        characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
