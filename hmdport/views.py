from http import client
from django.shortcuts import render,redirect
from  hmdport.models import contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def viewcontact(request):
    if request.method == 'POST':
        clientnames = request.POST.get('client')
        emails = request.POST.get('em')
        subjects = request.POST.get('sub')
        messages = request.POST.get('msg')
        obj = contact.objects.create(clientname=clientnames,email=emails,subject=subjects,message=messages)
        obj.save()
        if obj:
            return HttpResponse('successfully sent message')
        else:
            return HttpResponse('Please enter correct details....')
    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def gallerysingle(request):
    return render(request,'gallery-single.html')

def gallery2(request):
    return render(request,'gallery2.html')
def gallery3(request):
    return render(request,'gallery3.html')
def gallery3(request):
    return render(request,'gallery3.html')
def gallery4(request):
    return render(request,'gallery4.html')
def gallery5(request):
    return render(request,'gallery5.html')
def gallery6(request):
    return render(request,'gallery6.html')
def gallery7(request):
    return render(request,'gallery7.html')

def services(request):
    return render(request,'services.html')