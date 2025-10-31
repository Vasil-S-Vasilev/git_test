from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from profiles.models import Profile
from django.urls import reverse_lazy
from profiles.forms import ProfileCreateForm, ProfileEditForm
from recipeTest.utils import get_user_object
# Create your views here.

class CreateProfileView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('home-page') # to cataloque-page


class DetailsProfileView(DetailView):
    template_name = 'profiles/details-profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_user_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Only published posts by this author
        profile = self.get_object()
        recipes = profile.recipes.all()
        context['recipes_count'] = recipes.count()
        return context

class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profiles/edit-profile.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_object()
