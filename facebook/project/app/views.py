from django.shortcuts import render,redirect
from . models import Student

# Create your views here.
def base(req):
    return render(req,'base.html')
def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')
        print(e,p)
        if e == 'admin@gmail.com' and p == 'admin':
            req.session['admin_e'] = e
            req.session['admin_p'] = p
            req.session['admin_n'] = 'admin'
            return render('dashboard')
        user = Student.objects.filter(email=e)
        if user:
            userdata=Student.objects.get(email=e)
            if p == userdata.password:
                id = userdata.id
                req.session['user_id']=id
                return redirect('dashboard')
            else:
                req.session['y']="Email and Password Not Match"
                return redirect('login')
        else:
            req.session['x']="Email is not registered"
            return redirect('register')
    y=req.session.get('y','')
    return render(req,'login.html',{'y':y})

    
def dashboard(req):
    return render(req,'dashboard.html')