from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail
def registration(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={"EUFO":EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMPFDO.is_valid() and NMUFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw_enc=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw_enc)
            MUFDO.save()
            
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            
            send_mail(
                "REGISTERED", #SUBJECT
                'REGISTRATION IS SUCCESS',# MESSAGE
                'venkatalaxmi625@gmail.com',  #senders email
                [MUFDO.email], #receivers email
                fail_silently=False #True
                
            )
            
            return HttpResponse("Registration is Success")
        else:
            HttpResponse("Invalid data")
    return render(request,"registration.html",d)
            
            
        
