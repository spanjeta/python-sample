from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from accounts.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def home(request):
    template_name = 'backend/site/index.html'
    if not request.user.is_superuser:
        return HttpResponseRedirect('admin/login')
    else: 
        return render(request, template_name, {})

    
@login_required
def user_index(request):
    template_name = 'backend/user/index.html'
   
    if not request.user.is_superuser:
        return HttpResponseRedirect('admin/login')
    else:
        user_list = User.objects.all()
        
        if user_list:
            if user_list.count() > 2:
                paginator = Paginator(user_list, 2)
            else:
                paginator = Paginator(user_list, user_list.count())
         
            if user_list.count() > 2:
                try:
                    users = paginator.page(page)
                except PageNotAnInteger:
                    users = paginator.page(1)
                except EmptyPage:
                    users = paginator.page(paginator.num_pages)
            else:
                users = user_list
        else:
            users = None
        
        return render(request, template_name, {'users' : users})

@login_required
def add_user(request):
    template_name = 'backend/user/add.html'
    if not request.user.is_superuser:
        return HttpResponseRedirect('admin/login')
    else:
        return render(request, template_name, {})
    
@login_required
def setting_index(request):
    template_name = 'backend/setting/index.html'
   
    if not request.user.is_superuser:
        return HttpResponseRedirect('admin/login')
    else:
        return render(request, template_name, {})
