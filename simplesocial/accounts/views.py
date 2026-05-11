from django.shortcuts import render
from django.urls import reverse_lazy #used for logins and logout
from . import forms # forms for signup
from django.views.generic import CreateView

# Create your views here.

class SignupView(CreateView):
        form_class = forms.UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'accounts/signup.html'
