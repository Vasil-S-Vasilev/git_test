from django.shortcuts import render
from django.views.generic import TemplateView
from recipeTest.utils import get_user_object
# Create your views here.



class HomePageView(TemplateView):
    template_name = 'home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_object()
        return context