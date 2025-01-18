#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Home page')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About page')
    return render(request, 'about.html')

def registration(request):
    # return HttpResponse('About page')
    return render(request, 'faculty_reg.html')

def attendance(request):
    # return HttpResponse('Home pag')
    return render(request, 'attendance.html')


def profile(request):
    # return HttpResponse('Home pag')
    return render(request, 'profile.html')

def salary_management(request):
    # return HttpResponse('Home pag')
    return render(request, 'salary_management.html')