from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings

def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'home.html')


# def signin(request):
#     if request.method == 'POST':
#         studentid = request.POST.get('studentid')
#         pass1 = request.POST.get('pass1')
#         x = Student.objects.filter(username=studentid,password=pass1)
#         if x:
#             return redirect('home')
#         else:
#             return render(request,'signin.html')
#     return render(request,'signin.html')






def signin(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        pass1 = request.POST.get('pass1')
        x = Student.objects.filter(username=studentid, password=pass1)
        if x:
            user = authenticate(request, username=studentid, password=pass1)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')






def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        studentid = request.POST['studentid']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        course = request.POST['course']
        images = request.FILES['images']

        x = Student.objects.create(name=name, email=email, password=pass1, username=studentid, course=course,images=images)
        subject = 'Registration successful'
        message = 'You have registered succesfully and account is created.'
        from_email = 'accalphilip10@gmail.com'
        recipient_list = [x.email,]
        send_mail(subject, message, from_email, recipient_list)
        x.save()
        return redirect('signin')
    return render(request,'register.html')


def view_details(request,pk):
    z = Student.objects.get(id=pk)
    return render(request,'details.html',{'z':z})