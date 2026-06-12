from django.shortcuts import render,redirect
from .models import Register
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        r=Register.objects.create(name=name,email=email,phone=phone,password=password,confirm_password=confirm_password)
        r.save()
        return redirect('login')
    return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        r=Register.objects.filter(name=name,password=password,email=email)
        if r:
            return redirect('blogpage')
    return render(request, 'login.html')
def blogpage(request):
    return render(request,'blogpage.html')

# Create your views here.
