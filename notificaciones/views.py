from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.http import HttpResponse
import urllib2
import json
from django.shortcuts import render
from django.core import serializers
from connections import HOST, WEB_PORT, IO_PORT
from django.core.serializers.json import DjangoJSONEncoder


def verify(request, session_id):
    session = Session.objects.get(session_key=session_id)
    uid = session.get_decoded().get('_auth_user_id')
    user = tipo.objects.filter(pk=uid).first()
    if user:
        response = {'webuser': user.username}
        return HttpResponse(json.dumps(response))
    # end if
    return HttpResponse(uid)
# end def
