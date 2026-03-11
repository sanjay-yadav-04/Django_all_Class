from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def mail(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        contact=req.POST.get('contact')
        query=req.POST.get('query')
        send_mail(
            "Subject here",
            email,
            email,
            ["sy2102004@gmail.com"],
            fail_silently=False,
        )
        return HttpResponse("MAil Done")
    