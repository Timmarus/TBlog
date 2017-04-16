"""TBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^login/', auth_views.login,
        {'template_name': 'account/templates/login.html'}, name="login"),
    url('^logout/', auth_views.logout,
        {'template_name': 'account/templates/logout.html'}, name="logout"),
    url(r'^password_change/$', auth_views.password_change,
        {'template_name': 'account/templates/password_change.html'}, name="password_change"),
    url('^password_change/done', auth_views.password_change_done,
        {'template_name': 'account/templates/password_change_done.html'},name="password_change_done"),
    url(r'^password_reset/$', auth_views.password_reset,
        {'template_name': 'account/templates/password_reset.html'}, name="password_reset"),
    url('^password_reset/done', auth_views.password_reset_done,
        {'template_name': 'account/templates/password_reset_done.html'}, name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'account/templates/reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^reset/done/$', auth_views.login,
        {'template_name': 'account/templates/reset_done.html'}, name="password_reset_complete"),
]
