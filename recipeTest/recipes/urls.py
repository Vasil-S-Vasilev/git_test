from django.urls import path, include
from recipes.views import RecipeCreateView, CataloqueView, RecipeDetailView, RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='create-recipe'),
    path('catalogue/', CataloqueView.as_view(), name='cataloque-page'),
    path('<int:recipe_id>/', include([
        path('details/', RecipeDetailView.as_view(), name='details-recipe'),
        path('edit/', RecipeEditView.as_view(), name='edit-recipe'),
        path('delete/', RecipeDeleteView.as_view(), name='delete-recipe'),
    ]))
]
