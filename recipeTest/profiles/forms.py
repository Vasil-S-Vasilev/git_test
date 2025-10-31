from profiles.models import Profile
from django import forms


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('bio', )

class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'bio', 'chef']