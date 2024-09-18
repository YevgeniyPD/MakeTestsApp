from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout, login
from .utils import *
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView
from .models import *
from users.forms import RegisterUserForm, LoginUserForm

class hometestsapp(DataMixin, ListView):
    model = Tests
    template_name = 'tests/base.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

class AddTest(DataMixin, ListView):
    model = Tests
    template_name = 'tests/addtest.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Создать тест")
        return dict(list(context.items()) + list(c_def.items()))

    # def form_valid(self, form):
    #     w = form.save(commit=False)
    #     w.author = self.request.user
    #     return super().form_valid(form)

class Test(DataMixin, ListView):
    model = Tests
    template_name = 'tests/tests.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Пройти тест")
        return dict(list(context.items()) + list(c_def.items()))

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'tests/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('tests:home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tests/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('tests:home')

def logout_user(request):
    logout(request)
    return redirect('tests:login')