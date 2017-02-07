from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import LandingSubscriber, LandingSubscriberForm, ArtistRegisterForm

from util import validate_email
import re

def signup(request):
    print "helloooo"
    if request.method == 'POST':
        form = ArtistRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['pass1']
            pass2 = form.cleaned_data['pass2']
            artist = Artist(email=email)
            if all([name, email, pass1, pass2] and pass1 == pass2):
                artist.name = name
                artist.email = email
            artist.save()
            return redirect('auth_login')
        return render(request, 'registration/registration_form.html', {'form':form})

# @login_required
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