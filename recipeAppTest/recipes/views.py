from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from recipes.models import Recipe
from django.urls import reverse_lazy
from recipes.forms import RecipeCreateForm, RecipeEditForm, RecipeDeleteForm
from recipeAppTest.utils import get_user_object
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipes/create-recipe.html'
    success_url = reverse_lazy('catalogue-page')

    def form_valid(self, form):
        form.instance.author = get_user_object()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        # form = self.get_form()
        # print(form.fields)  # test
        # print(context['form'])  # test
        return context

class CataloqueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'

    # new added
    def get_queryset(self):
        if self.request.user.has_perm('recipes.can_approve_recipes'):
            return Recipe.objects.all()
        return Recipe.objects.filter(approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        # context['can_approve'] = self.request.user.has_perm('recipes.can_approve_recipes')  
        return context

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/details-recipe.html'
    context_object_name = 'recipe'
    pk_url_kwarg = 'recipe_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()

        ingredients = self.object.ingredients.split(', ')
        context['ingredients_list'] = ingredients  #  ['shkembe', 'mlqko', 'cherven piper']
        return context


class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeEditForm
    template_name = 'recipes/edit-recipe.html'
    context_object_name = 'recipe'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('catalogue-page')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        if not self.request.user.has_perm('recipes.can_approve_recipes'):
            form.fields.pop('approved', None)

        return form
        

    def form_valid(self, form):
        if not self.request.user.has_perm('recipes.can_approve_recipes'):
            form.instance.approved = False

        return super().form_valid(form)



    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context

class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = 'recipes/delete-recipe.html'
    pk_url_kwarg = 'recipe_id'
    success_url = reverse_lazy('catalogue-page')

    def get_initial(self):
        return self.object.__dict__
    
    def form_invalid(self, form):
        return self.form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context



