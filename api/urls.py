from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", views.apiOverview, name="overview"),
    path("note-list/<str:pk>/", views.noteList.as_view(), name="list"),
    path("note-detail/<str:pk>/", views.noteDetail, name="detail"),
    path("create-note/", views.createNote.as_view(), name="create"),
    path("update-note/<str:pk>/", views.updateNote, name="update"),
    path("delete-note/<str:pk>/", views.deleteNote, name="delete"),
    path("create-user/", views.createUser, name="create-user"),
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
