from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team
# Create your views here.
# def home(requset):
#     return HttpResponse("helloo Home")
#
# def about(requset):
#     return render(requset,"about.html")
#
# def contact(requset):
#     return render(requset,"contact.html")
#
# def details(requset):
#     return render(requset,"details.html")
#
# def thanks(requset):
#     return render(requset,"thanks.html")

def demo(request):
    # name="india"
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,"result.html",{'add':res ,'sub':res1 ,'mul':res2 ,'div':res3})
