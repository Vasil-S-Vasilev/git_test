from django.urls import path, include
from books import views
from rest_framework.routers import DefaultRouter
from books.views import PublisherViewSet


router = DefaultRouter()  # used for generating urls dynamically 
router.register('', PublisherViewSet)


urlpatterns = [
    path('books/', views.ListBookView.as_view(), name = 'books_list'),
    # path('books/', views.list_books_view, name = 'index')
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
    path('publisher-links/', views.PublisherHyperlinkView.as_view(), name='publisher-link'),
    path('publishers/', include(router.urls)),
]