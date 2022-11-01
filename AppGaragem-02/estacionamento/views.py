import json
import re
from re import U
from urllib.parse import quote_plus, urlencode

from authlib.integrations.django_client import OAuth
from decouple import config
from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

global session
session = None

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=config('APP_CLIENT_ID'),
    client_secret=config('APP_CLIENT_SECRET'),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{config('APP_DOMAIN')}/.well-known/openid-configuration",
)

def home(request):
    if not session:
        return render(request, 'home.html')
    else:
        return redirect('/profile')

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    global session
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    session = request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("profile")))

def profile(request):
    return render(
        request,
        "profile.html",
        context={
            "session": session,
            "pretty": json.dumps(session, indent=4),
        },
    )

def logout(request):
    global session
    session = request.session.clear()
    request.session.clear()
    django_logout(request)
    domain=config('APP_DOMAIN')
    client_id=config('APP_CLIENT_ID')
    return_to='http://localhost:5000'
    return HttpResponseRedirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")
