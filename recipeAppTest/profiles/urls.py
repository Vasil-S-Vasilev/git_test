from django.urls import path
from profiles.views import CreateProfileView, DetailsProfileView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name="create-profile"),
    path('details/', DetailsProfileView.as_view(), name="details-profile"),
    path('edit/', ProfileEditView.as_view(), name="edit-profile"),
    path('delete/', ProfileDeleteView.as_view(), name="delete-profile"),
]