from django.shortcuts import render

# Create your views here.
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView,View
from .forms import LoginForm,RegForm
from django.contrib.auth import authenticate,login


class HomeView(FormView):
    template_name='login.html'
    form_class=LoginForm

    def post(self, request, *args ,**kwargs):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return redirect('customerhome')
            else:
                return redirect('home')
                


class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,'reg.html',{'form':form})
    
    def post(self,request):
        form_data=RegForm(data=request.POST)
        print(form_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('home')
        else:
            return render(request,'reg.html',{'form':form_data})
    

