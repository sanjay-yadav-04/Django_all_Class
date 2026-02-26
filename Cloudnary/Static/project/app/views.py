from django.shortcuts import render,redirect
from .models import Data
# Create your views here.
def landing(req):
    return render(req,'landing.html')
def data(req):
    if req.method=="POST":
       Data.objects.create(
           name=req.POST.get('name'),
           email=req.POST.get('email'),
           age=req.POST.get('age'),
           image=req.POST.get('image'),
           video=req.POST.get('video'),
           pdf=req.POST.get('pdf')
        )
       return render(req,'showdata.html')
    return redirect('landing')
def showdata(req):
    data = Data.objects.all()
    return render(req, 'showdata.html', {'data': data})
