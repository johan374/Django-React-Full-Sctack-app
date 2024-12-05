from django.urls import path  # Import the `path` function to define URL patterns
from . import views  # Import the views module from the current application

# Define the URL patterns for this app
urlpatterns = [
    # URL for listing and creating notes
    path(
        "notes/",  # The URL endpoint is "notes/"
        views.NoteListCreate.as_view(),  # Connect this endpoint to the `NoteListCreate` view, which handles GET (list) and POST (create) requests
        name="note-list"  # Assign a name to this URL pattern for easier reference in templates or reverse lookups
    ),

    # URL for deleting a specific note
    path(
        "notes/delete/<int:pk>/",  # The URL endpoint is "notes/delete/<int:pk>/". 
        # `<int:pk>` is a path converter that captures an integer parameter called `pk` (primary key of the note to delete).
        views.NoteDelete.as_view(),  # Connect this endpoint to the `NoteDelete` view, which handles DELETE requests for a specific note
        name="delete-note"  # Assign a name to this URL pattern for easier reference in templates or reverse lookups
    ),
]
