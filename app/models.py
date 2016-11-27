from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Provider(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100)

class LandingSubscriber(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    class Meta:
      db_table = "landing_subscriber"

class LandingSubscriberForm(ModelForm):
    class Meta:
        model = LandingSubscriber
        fields = ['first_name', 'last_name', 'email']


  		  