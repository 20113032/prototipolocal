from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from posts.views import register, register_success, logout_page, home, create, create_success

urlpatterns = [
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
    url(r'^home/$', home, name='home'),
    url(r'^create/$', create, name='create'),
    url(r'^create/success/$', create_success, name='create_success')
]
