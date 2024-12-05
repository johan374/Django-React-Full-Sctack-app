from django.shortcuts import render
from django.contrib.auth.models import User  # Import the User model from Django's auth system
from rest_framework import generics  # Import the generics module from the Django REST framework
from .serializers import UserSerializer, NoteSerializer  # Import the UserSerializer from your app's serializers
from rest_framework.permissions import IsAuthenticated, AllowAny  # Import permission classes for controlling access
from .models import Note  # Import the Note model from your application

# Define a view for listing and creating notes
class NoteListCreate(generics.ListCreateAPIView):
    """
    This view handles two operations:
    1. Listing all notes created by the authenticated user (GET request).
    2. Creating a new note for the authenticated user (POST request).
    """
    serializer_class = NoteSerializer  # Specify the serializer to use for this view
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users only

    def get_queryset(self):
        """
        Override the default queryset to return only notes created by the authenticated user.
        This ensures users can only see their own notes.
        """
        user = self.request.user  # Get the currently authenticated user from the request
        return Note.objects.filter(author=user)  # Query notes where the `author` matches the authenticated user

    def perform_create(self, serializer):
        """
        Override the default create behavior to automatically set the author field for new notes.
        This ensures the note is linked to the authenticated user who created it.
        """
        if serializer.is_valid():  # Check if the data sent by the client is valid
            serializer.save(author=self.request.user)  # Save the note with the authenticated user as the author
        else:
            # If the data is invalid, print errors to the console (useful for debugging)
            print(serializer.errors)

# Define a view for deleting notes
class NoteDelete(generics.DestroyAPIView):
    """
    This view handles deleting a note.
    Only authenticated users can access this view, and they can delete only their own notes.
    """
    serializer_class = NoteSerializer  # Specify the serializer to use for this view
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users only

    def get_queryset(self):
        """
        Override the default queryset to restrict the deletion operation to notes owned by the authenticated user.
        """
        user = self.request.user  # Get the currently authenticated user from the request
        return Note.objects.filter(author=user)  # Query notes where the `author` matches the authenticated user
    

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """
    View for creating a new user using the provided serializer.
    """
    # Specify the queryset to be used by this view. 
    # This means the view will operate on the `User` model and will allow interaction with all users in the database.
    queryset = User.objects.all()

    # Specify which serializer to use for this view. The serializer transforms model data into JSON (or other formats).
    # In this case, we want to use the `UserSerializer` to create or validate user data.
    serializer_class = UserSerializer

    # Permission class to specify what kind of access control is required to use this view.
    # `AllowAny` means that anyone (authenticated or not) can access this view.
    # This is important for an endpoint that allows user creation, as you want open access to register new users.
    permission_classes = [AllowAny]  
