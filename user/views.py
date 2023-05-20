from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import RegisterForm, LoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
class RegisterView(View):
    def get(self, request):
        
        form = RegisterForm()
        
        return render(request, "user/register.html", {
            "form":form
        })
    def post(self, request):

        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = User.objects.create_user(request.POST['user_name'], request.POST['email'], request.POST['password'])
            new_user.save()
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "user/register.html", {"form":form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        
        return render(request, "user/login.html", {
            "form":form
        })
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            auth_user = authenticate(username=request.POST["user_name"], password=request.POST["password"])
        else:
            return render(request, "user/login.html", {
            "form":form
        })

        if auth_user is not None:
            login(request, auth_user)
            return HttpResponseRedirect(reverse("library-entry"))
        else:
            HttpResponseRedirect(reverse("login-message"), {"User cannot be authenticated!"})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))