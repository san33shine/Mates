from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'

class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'core/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('core:core_index'))
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('core:core_index'))
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('core:core_index'))


class ChangePasswordView(View):
    form_class = PasswordChangeForm
    template_name = 'core/change_password.html'
    success_url = reverse_lazy('core:core_index')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class(user=request.user)
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})