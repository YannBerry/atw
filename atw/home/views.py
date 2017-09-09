from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from atw.home.forms import RegistrationForm
from atw.map.models import TripStage


def home(request):
    print(request.POST)
    return render(request, 'home/home.html')


def sign_in(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('my_account'))
        else:
            print("The password is valid, but the account has been disabled!")
    # else:
        # Return an 'invalid login' error message.
        # return HttpResponseRedirect(reverse('sign_in_or_register'))
    args = {}
    args['username'] = request.user.username
    return render(request, 'home/sign_in.html', args)


def sign_out(request):
    logout(request)
    return render(request, 'home/sign_out.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sign_in'))
    args = {}
    args['form'] = RegistrationForm()
    return render(request, 'home/register.html', args)


def my_account(request):
    args = {}
    username = request.user.username
    args['username'] = username
    args['trip_stage_added_by_user'] = TripStage.objects.filter(added_by=username)
    return render(request, 'home/my_account.html', args)
