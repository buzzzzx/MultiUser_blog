from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .forms import RegisterForm
from .models import UserProfile

# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "account/register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get("email", "")
            if UserProfile.objects.filter(email=email):
                return render(request, "account/register.html", {"register_form": register_form, "msg": "邮箱已被注册！"})

            password = request.POST.get("password", "")
            username = request.POST.get("username", "")
            user = UserProfile()
            user.username = username
            user.email = email
            user.password = make_password(password)
            ###
            user.is_active = True
            user.save()

            return render(request, "account/register_done.html", {'user': user})
        else:
            return render(request, "account/register.html", {"register_form": register_form})


