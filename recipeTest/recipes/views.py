from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recipes.models import Recipe
from django.urls import reverse_lazy
from recipeTest.utils import get_user_object
from recipes.forms import RecipeCreateFrom, RecipeEditForm, RecipeDeleteForm

# Create your views here.

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateFrom
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('cataloque-page')

    def form_valid(self, form):
        form.instance.author = get_user_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context

class CataloqueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    context_object_name = 'recipe'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        
        ingredients = self.object.ingredients.split(', ')  #  ['shkembe', 'mlqko', 'cherven piper']
        context['ingredients_list'] = ingredients

        return context

class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = 'recipes/edit-recipe.html'
    pk_url_kwarg = 'recipe_id'
    context_object_name = 'recipe'
    success_url = reverse_lazy('cataloque-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        print(type(context['form'].fields))  # test
        return context


class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = 'recipes/delete-recipe.html'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('cataloque-page')

    
    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context