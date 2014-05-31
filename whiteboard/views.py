from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from forms import *
from models import *
import datetime,json
from django.core import serializers

###################################
## register views 
###################################
def register_user(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			obj = form.save(commit=False)
			user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
			form.save()
			user.save()
			user_login = authenticate(username=cd['username'],password=cd['password'])
			if user_login is not None:
				if user_login.is_active:
					login(request,user_login)
					return redirect('/codebin/whiteboard/')
	else:
		form = RegistrationForm()
	return render(request,'index.html',{'reg_form': form, })

