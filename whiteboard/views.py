from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import *
from models import *
import datetime,json
from django.core import serializers

###################################
## register views 
###################################
def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user_data = form.save()
			user_login = authenticate(username=request.POST['username'], password=request.POST['password1'])
			if user_login is not None:
				if user_login.is_active:
					login(request,user_login)
					return redirect('/home/')
	else:
		form = UserCreationForm()
	return render(request,'index.html',{'reg_form': form, })

@login_required(login_url='/home/')
def post_message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			msg_id = form.customSave(User.objects.filter(username=request.user.username)[0]).pk
			return redirect('/whiteboard/%s/' % msg_id)
	else:
		form = MessageForm()
	return render(request, 'create_message.html', {'form': form})


# main view
def home_view(request,filter_type=None):
	if filter_type is None:
		messages = Message.objects.all()
	elif filter_type == 'latest':
		messages = Message.objects.all().order_by('-datetime')
	paginator = Paginator(messages, 25)
	page = request.GET.get('page')
	try:
		msgs = paginator.page(page)
	except PageNotAnInteger:
		msgs = paginator.page(1)
	except EmptyPage:
		msgs = paginator.page(paginator.num_pages) 
	return render(request,'main.html', {'messages':msgs})


def view_message(request, id):
	message = Message.objects.filter(pk=id)[0]
	return render(request,'view_message.html', {'message': message})

def filter_messages(request, term):
	messages = Message.objects.filter(language=term)
	return render(request, 'main.html', {'messages':messages})

def filter_msg_user(request, username):
	userid = User.objects.filter(username=username)[0]
	messages = Message.objects.filter(user=userid)
	return render(request, 'main.html', {'messages':messages})

def login_user(request):
	form = UserLoginForm()
	if request.method == 'POST':
		#form = UserLoginForm(request.POST)
		#if form.is_valid():
		#cd = form.cleaned_data
		user_login = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user_login is not None:
			login(request,user_login)
			return redirect('/home/')
	return redirect('/home/')

def logout_user(request):
	logout(request)
	return redirect('/home/')