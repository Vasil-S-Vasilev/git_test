from django.urls import path, include
from recipes.views import RecipeCreateView

urlpatterns = [
    path('create', RecipeCreateView.as_view(), name='create-recipe'),
]
