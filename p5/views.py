from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<marquee>welcome to views page</marquee>")
def home(request):
    return render(request,"pro1.html")
def second(request):
    return render(request,'directory/pro2.html')
def third(request):
    return render(request,'directory/pro3.html',context={'data':'Ranateja','name':'ranateja'})
def fourth(request):
    fruits=['apple','mango', 'strawberry']
    return render(request,'directory/pro4.html',{'fruits':fruits})
def fifth(request):
    return render(request,'directory/pro5.html',{'a':10,'b':20})