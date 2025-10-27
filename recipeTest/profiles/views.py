from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from profiles.models import Profile
from django.urls import reverse_lazy
from profiles.forms import ProfileCreateForm
# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('home-page') # to cataloque-page