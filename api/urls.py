from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("note-list/", views.noteList, name="list"),
    path("note-detail/<str:pk>/", views.noteDetail, name="detail"),
    path("create-note/", views.createNote, name="create"),
    path("update-note/<str:pk>/", views.updateNote, name="update"),
    path("delete-note/<str:pk>/", views.deleteNote, name="delete"),
]
