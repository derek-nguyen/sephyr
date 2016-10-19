from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import LandingSubscriber
from .models import LandingSubscriberForm

import re

def index( request ):
	return render(request, 'index.html', None)

def thankyou( request ):
    # if this is a POST request, we need to process the form data
    if request.method == 'POST':
        form = LandingSubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if email and len(email):
                check = re.match()
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
	

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False