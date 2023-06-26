from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/note-list/",
        "Detailed View": "/note-detail/<str:pk>/",
        "Create": "/note-create/",
        "Update": "/note-update/<str:pk>/",
        "Delete": "/note-delete/<str:pk>/",
        "Create user": "/create-user/",
        "Login user": "/login-user/",
    }

    return Response(api_urls)


class noteList(APIView):
    def get(self, request, pk, Format=None):
        notes = Note.objects.filter(user=pk)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def noteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


class createNote(APIView):
    def post(self, request, Format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(["POST"])
def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response("Object deleted successfully")


@api_view(["POST"])
def createUser(request):
    serializer = UserSerializer(request.data)
    username = serializer.data.get("username")
    password = serializer.data.get("password")
    email = serializer.data.get("email")
    print(username, email, password)
    if (
        User.objects.filter(username=username).exists()
        or User.objects.filter(email=email).exists()
    ):
        return Response(data="Username or email already exists", status=400)
    else:
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user.save()
        auth.login(request, user)
        return Response("User created successfully")
