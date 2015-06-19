from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from atw.home.forms import RegistrationForm

def home(request):
	return render_to_response('home/home.html')

def project(request):
	return render_to_response('home/project.html')

def ad(request):
	return render_to_response('home/ad.html')

def wm_fr(request):
	return render_to_response('home/wm_fr.html')

def community(request):
	return render_to_response('home/community.html')

def sign_in(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse('my_account'))
		else:
			print("The password is valid, but the account has been disabled!")
	#else:
	    # Return an 'invalid login' error message.
	    # return HttpResponseRedirect(reverse('sign_in_or_register'))
	args = {}
	args.update(csrf(request))
	args['username'] = request.user.username
	return render_to_response('home/sign_in.html', args)

def sign_out(request):
	logout(request)
	return render_to_response('home/sign_out.html')

def register(request):
	if request.method == 'POST':
		form =  RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('sign_in'))
	args = {}
	args.update(csrf(request))
	args['form'] = RegistrationForm()
	return render_to_response('home/register.html', args)

def my_account(request):
	args = {}
	args['username'] = request.user.username
	return render_to_response('home/my_account.html', args)
