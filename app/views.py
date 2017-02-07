from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import LandingSubscriber
from .models import LandingSubscriberForm

from util import validate_email
import re

from forms import Signup_form

def signup(request):
    print "helloooo"
    form = Signup_form()

    name = request.POST.get('name','')
    email = request.POST.get('email', '')
    pass1 = request.POST.get('pass1', '')
    pass2 = request.POST.get('pass2', '')

    # Do some validations here
    user = Artist.objects.create_user(name, email, pass2)
    if user:
        user.save()

    return render(request, 'signup.html', {'form': form})

@login_required
def index( request ):
    return render(request, 'index.html', None)

def landing( request ):
    return render(request, 'landing.html', None)

def thankyou( request ):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        form = LandingSubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not validate_email(email):
                return render(request, 'thankyou.html', { 'status': 'invalid_email'})
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            sub = LandingSubscriber(email=email)
            if all([first_name, last_name]):
                sub.first_name = first_name
                sub.last_name = last_name
            sub.save()
            return render(request, 'thankyou.html', {'sub':sub})
        return redirect('landing')