from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def set(req):
    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        p = req.POST.get('pass')
        response = render(req,'landing.html')
        response.set_cookie('name',n,max_age=60*60)
        response.set_cookie('email',e)
        response.set_cookie('pass',p)
        return response
    return render(req,'set.html')
        
def get(req):
    print(req.COOKIES)
    c=req.COOKIES.get('csrftoken')
    n=req.COOKIES.get('name')
    e=req.COOKIES.get('email')
    p=req.COOKIES.get('password')
    t=req.COOKIES.get('Sanjay','guest')
    print(c,n,e,p,t)
    return render(req,'get.html',{'name':n,'email':e,'password':p,'demo':t})
def delete(req):
    response=render(req,'delete.html')
    if 'name' in req.COOKIES:
        response.delete_cookie('name')
    if 'email' in req.COOKIES:
        response.delete_cookie('email')
    if 'password' in req.COOKIES:
        response.delete_cookie('password')
    return response