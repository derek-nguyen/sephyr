from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
    url(r'^accounts/', include('allauth.urls'))
]

# ^ ^accounts/ ^ ^signup/$ [name='account_signup']
# ^ ^accounts/ ^ ^login/$ [name='account_login']
# ^ ^accounts/ ^ ^logout/$ [name='account_logout']
# ^ ^accounts/ ^ ^password/change/$ [name='account_change_password']
# ^ ^accounts/ ^ ^password/set/$ [name='account_set_password']
# ^ ^accounts/ ^ ^inactive/$ [name='account_inactive']
# ^ ^accounts/ ^ ^email/$ [name='account_email']
# ^ ^accounts/ ^ ^confirm-email/$ [name='account_email_verification_sent']
# ^ ^accounts/ ^ ^confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
# ^ ^accounts/ ^ ^password/reset/$ [name='account_reset_password']
# ^ ^accounts/ ^ ^password/reset/done/$ [name='account_reset_password_done']
# ^ ^accounts/ ^ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
# ^ ^accounts/ ^ ^password/reset/key/done/$ [name='account_reset_password_from_key_done']
# ^ ^accounts/ ^social/
# ^admin/