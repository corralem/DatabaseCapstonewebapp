from django.shortcuts import render, HttpResponse, render_to_response, render
from django.template import loader


# Create your views here.




def home (request):
    return render(request, 'home.html')



def login (request):
    return render(request, 'login.html')


def signup (request):
    return render(request, 'signup.html')