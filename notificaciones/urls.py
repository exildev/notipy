from django.conf.urls import include, url
import views
import forms

urlpatterns = [
	url(r'^verify/(?P<session_id>\w+)/$', views.verify),
]