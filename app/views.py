from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LandingSubscriber
from .models import LandingSubscriberForm

from util import validate_email
import re

def index( request ):
	return render(request, 'index.html', None)

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
    else:
        return redirect('index')

def subscribe( request ):
    return HttpResponse("got to subscribe function")