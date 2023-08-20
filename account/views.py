from django.shortcuts import render
from .form import userRegisterForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
# Create your views here.

class userRegistrationView(FormView):
    template_name = 'account/register.html'
    form_class = userRegisterForm
    success_url = reverse_lazy('register')
    def form_valid(self,form) :
        user = form.save()
        login (user)
        return super().form_valid(form)
    