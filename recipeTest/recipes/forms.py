from django import forms
from recipes.models import Recipe
from recipeTest.mixins import PlaceholderMixin, ReadOnlyMixin


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('author',)


class RecipeCreateFrom(PlaceholderMixin, RecipeBaseForm):
    custom_placeholders = {
        'ingredients': 'ingredient1, ingredient2, ...',
        'instructions': 'Enter detailed instructions here...',
        'image_url': 'Optional image URL here...'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # this calls self.add_placeholders()

        
        # explicitly remove the placeholder
        self.fields['title'].widget.attrs.pop('placeholder', None)
        self.fields['cuisine_type'].widget.attrs.pop('placeholder', None)

        
        # Set help text and password masking
        self.fields['ingredients'].help_text = "Ingredients must be separated by a comma and space." 
        self.fields['cooking_time'].help_text = "Provide the cooking time in minutes."

class RecipeEditForm(PlaceholderMixin, RecipeBaseForm):
    pass


class RecipeDeleteForm(ReadOnlyMixin, RecipeBaseForm):
    read_only_fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']


