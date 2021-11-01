from django.http import HttpResponse
from django.shortcuts import render
from . models import place
# Create your views here.
def fun(request):
    # return httpResponse("hello World")
    # return render(request,"index.html")
    obj=place.objects.all()
    return render(request, "index.html",{'results':obj})

def addition(request):
    num1=int(request.GET["num1"])
    num2=int(request.GET["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3} )