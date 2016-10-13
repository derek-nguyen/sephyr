from django.db import models
from django.forms import ModelForm

class LandingSubscriber(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)

class LandingSubscriberForm(ModelForm):
    class Meta:
        model = LandingSubscriber
        fields = ['first_name', 'last_name', 'email']