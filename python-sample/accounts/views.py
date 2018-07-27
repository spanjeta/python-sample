from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as auth_login


def login(request):
    template = 'accounts/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username= username, password=password)
        auth_login(request, user)

    return render(request, template)