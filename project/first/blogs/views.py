import django
from django.shortcuts import render
from samba.dcerpc.smb_acl import user

from .form import SignUpForm
from .form import Contact_form
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp


# Create your views here.

def home(request):
    title = 'Welcome'

   # if request.user.is_authenticated():
      #    title = 'welcome %s'%(request.user)

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
        if not instance.full_name:
            instance.full_name='alsum'
            instance.save()
            print instance.email
            print instance.timestamp
    context = {
        'title': title,
        'form': form,

    }
    if request.user.is_authenticated or request.user.is_staffed :
        print(SignUp.objects.all())
        context={
            "queryset":[123,123]
        }


    return render(request,"home.html",context)

def contact(request):
    form = Contact_form(request.POST or None )
    if form.is_valid():
       # for key , value in form.cleaned_data.iteritems() :
        #    print key , value
        form_email = form.cleaned_data.get('email')
        form_message =form.cleaned_data.get('message')
        form_full_name =form.cleaned_data.get('full_name')
        Subject = 'Mail form django'

        from_email =settings.EMAIL_HOST_USER
        to_email = [form_email]
        contact_message ="%s %s via %s " %(form_full_name , form_message , form_email)
        send_mail(Subject,contact_message,form_email,to_email,fail_silently=True)

    context = {
            'form' : form,
        }
    return render(request,"form.html",context)

