from django.urls import path, include
from recipes.views import RecipeCreateView, CataloqueView, RecipeDetailsView, RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='create-recipe'),
    path('catalogue/', CataloqueView.as_view(), name='catalogue-page'),
    path('<int:recipe_id>/', include([
        path('details/', RecipeDetailsView.as_view(), name='details-recipe'),
        path('edit/', RecipeEditView.as_view(), name='edit-recipe'),
        path('delete/', RecipeDeleteView.as_view(), name='delete-recipe')
    ]))
]
