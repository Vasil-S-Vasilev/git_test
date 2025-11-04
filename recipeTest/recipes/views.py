from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recipes.models import Recipe
from django.urls import reverse_lazy
from recipeTest.utils import get_user_object
from recipes.forms import RecipeCreateFrom

# Create your views here.

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateFrom
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('home-page')  # to cataloque-page

    def form_valid(self, form):
        form.instance.author = get_user_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context
