from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "List": "/note-list/",
        "Detailed View": "/note-detail/<str:pk>/",
        "Create": "/note-create/",
        "Update": "/note-update/<str:pk>/",
        "Delete": "/note-delete/<str:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def noteList(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def noteDetail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def createNote(request):
    serializer = NoteSerializer(data=request.data)
    print(request.data)

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
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        username = request.GET["username"]
        password = request.GET["password"]
        email = request.GET["email"]
        if User.objects.filter(username=username).exists():
            return Response("Username already exists")
        else:
            serializer.save()
            return Response("User created successfully")
    else:
        return Response("Invalid data")


@api_view(["POST"])
def loginUser(request):
    user = auth.authenticate(
        username=request.get["username"], password=request.get["password"]
    )
    if user is not None:
        auth.login(user)
        return Response(user)
    else:
        return Response("Invalid credentials")
