from django.shortcuts import render, HttpResponse
from datetime import datetime
from app1.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    #return HttpResponse("this is homepage")
    return render(request,'index.html',context)

def about(request):
     return render(request,'about.html')
    #return HttpResponse("this is about page")    

def services(request):
     return render(request,'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact1=contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact1.save()
        messages.success(request,'Your query has been posted!')
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")        