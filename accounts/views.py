from django.shortcuts import redirect, render
from .models import Profile
from .forms import SignupForm
from django.contrib.auth import authenticate , login
from .models import Info
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect ('/accounts/profile')
    else :
        form = SignupForm()

    return render(request ,'registration/signup.html', {'form':form})

def profile(request):
    profile = Profile.objects.get( user = request.user )
    return render(request , 'profile/profile.html' , {'profile' : profile})

    
def send_message(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    return render(request , 'contact/contact.html' , {
        
    })