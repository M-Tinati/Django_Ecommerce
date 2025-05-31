from django.shortcuts import render , redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
class AccountsView(View):
    form_class = UserRegisterForm
    template_name = 'signup.html'
        
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password1'])
            return redirect('home:main_home')
        
        return render(request,self.template_name,{'form':form})

class UserLogOutView(LoginRequiredMixin , View):
    def get(self,request):
        logout(request)
        return redirect('home:main_home')
        
        

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'login.html'
        
    def get(self,request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password1'])
            if user is not None:
                login(request,user)
                return redirect('home:main_home')
        
        return render(request,self.template_name,{'form':form})
