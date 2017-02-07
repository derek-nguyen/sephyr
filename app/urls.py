from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^accounts/register/$', views.signup, name='signup')
]

# registration naming

# ^ ^accounts/ ^register/$ [name='registration_register']
# ^ ^accounts/ ^register/closed/$ [name='registration_disallowed']
# ^ ^accounts/ ^login/$ [name='auth_login']
# ^ ^accounts/ ^logout/$ [name='auth_logout']
# ^ ^accounts/ ^password/change/$ [name='auth_password_change']
# ^ ^accounts/ ^password/change/done/$ [name='auth_password_change_done']
# ^ ^accounts/ ^password/reset/$ [name='auth_password_reset']
# ^ ^accounts/ ^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='auth_password_reset_confirm']
# ^ ^accounts/ ^password/reset/complete/$ [name='auth_password_reset_complete']
# ^ ^accounts/ ^password/reset/done/$ [name='auth_password_reset_done']
# ^admin/