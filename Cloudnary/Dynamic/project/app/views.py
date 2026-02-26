from django.shortcuts import render, redirect
from .models import Data

def landing(req):
    return render(req, 'landing.html')

def data(req):
    if req.method == "POST":
        name = req.POST.get('name')
        email = req.POST.get('email')
        age = req.POST.get('age')

        image = req.FILES.get('image')
        video = req.FILES.get('video')
        pdf = req.FILES.get('pdf')

        Data.objects.create(
            name=name,
            email=email,
            age=age,
            image=image,
            video=video,
            pdf=pdf
        )

        return redirect('showdata')

    return redirect('landing')
def showdata(req):
    data=Data.objects.all()
    return render(req,'showdata.html',{'data':data})