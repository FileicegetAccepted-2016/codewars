from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import View
from .form import UserForm


def index(request):
    return render(request, 'RITCSE_codeWars/Home.html')


def all_submission(request):
    return render(request, 'RITCSE_codeWars/AllSubmissions.html')

def your_submissions(request):
    return render(request, 'RITCSE_codeWars/YourSubmissions.html')


def your_code(request):
    return render(request, 'RITCSE_codeWars/YourCode.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'RITCSE_codeWars/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(commit=True)


def login_user(request):
    return render(request,'RITCSE_codeWars/Login.html')


def authenticate_user(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return HttpResponseRedirect(reverse('Login'))
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(reverse('Login') + '?error=true')
    login(request, user)
    return HttpResponseRedirect(reverse('Index'))

