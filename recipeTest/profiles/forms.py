from profiles.models import Profile
from django import forms


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio', )

class ProfileCreateForm(ProfileBaseForm):
    pass