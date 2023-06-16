from django.shortcuts import render
from .models import Note
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer

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
