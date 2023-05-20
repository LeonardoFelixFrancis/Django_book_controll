from django.urls import path
from . import views

urlpatterns = [
    path("", views.LibraryIndexView.as_view(), name="library-entry"),
    path("filter-books", views.FilterBooksView.as_view(), name="form-filter"),
    path("open-book/<int:id>", views.OpenBookFilter.as_view(), name="open-book"),
    path("edit-book/<int:id>", views.EditBookView.as_view(), name="edit-book"),
    path("delete-book<int:id>", views.DeleteBookView.as_view(), name="delete-book")
]
