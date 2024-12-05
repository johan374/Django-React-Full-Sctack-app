// Import React hooks for managing state and side effects
import { useState, useEffect } from "react";

// Import the `api` Axios instance for making HTTP requests
import api from "../api";
import Note from "../components/Note"
import "../styles/Home.css"

// Define the `Home` functional component
function Home() {
    // State to store the list of notes
    const [notes, setNotes] = useState([]); // Initialize `notes` as an empty array
    // State to store the content of a new note (if needed for creation)
    const [content, setContent] = useState(""); // Initialize `content` as an empty string
    // State to store the title of a new note (if needed for creation)
    const [title, setTitle] = useState(""); // Initialize `title` as an empty string

    // `useEffect` runs the `getNotes` function after the component mounts
    // It ensures that the notes are fetched when the `Home` component is rendered
    useEffect(() => {
        getNotes(); // Fetch notes from the API
    }, []); // Empty dependency array ensures this runs only once, like componentDidMount

    // Function to fetch notes from the API
    const getNotes = () => {
        api // Use the pre-configured Axios instance
            .get("/api/notes/") // Send a GET request to the `/api/notes/` endpoint
            .then((res) => res.data) // Extract the response data from the API response
            .then((data) => {
                // Update the `notes` state with the retrieved data
                setNotes(data);
                console.log(data); // Log the notes data to the console (for debugging)
            })
            .catch((err) => {
                console.error(err); // Log any error that occurs during the request
            });
    };

    const deleteNote = (id) => {
        api
            .delete(`/api/notes/delete/${id}/`) // Sends a DELETE request to the API to delete a note by its `id`.
            .then((res) => {
                if (res.status == 204) // HTTP status 204 means "No Content," indicating successful deletion.
                    alert("Note deleted!"); // Notify the user about the successful deletion.
                else 
                    alert("Filed to delete note"); // Notify the user if something went wrong.
                getNotes(); // Refresh the list of notes to reflect the changes.
            })
            .catch((error) => alert(error)); // Handle any error that occurs during the request.
        
    };
    
    
    const createNote = (e) => {
        e.preventDefault(); 
        // Prevents the default form submission behavior (e.g., page reload).
    
        api
            .post("/api/notes/", { content, title }) 
            // Sends a POST request to the "/api/notes/" endpoint with the `content` and `title` data.
    
            .then((res) => {
                if (res.status == 201) {
                    // If the server responds with HTTP status 201 (Created), the note was successfully created.
                    alert("Note created!"); 
                    // Display a success message to the user.
    
                    getNotes(); 
                    // Refreshes the notes list by calling the `getNotes()` function, ensuring the new note appears.
                } else {
                    // If the status is not 201, show an error message.
                    alert("Failed to make note.");
                }
            })
    
            .catch((err) => {
                // Handles any errors that occur during the request.
                console.error("Full error:", err);
                // Logs the full error object for debugging.
    
                console.error("Error response:", err.response);
                // Logs the server's response, which typically contains the error details.
    
                alert(err.response 
                    ? JSON.stringify(err.response.data) 
                    : "Note creation failed"
                );
                // If the server sent an error response, display the error details; otherwise, show a generic message.
            });
    };
    
   

return (
    <div> {/* This is the container for the entire component. */}
        <div> 
            {/* This inner `div` contains the list of notes and the section title. */}

            <h2>Notes</h2> 
            {/* A header that indicates the section is about notes. */}

            {notes.map((note) => (
                <Note note={note} onDelete={deleteNote} key={note.id} />
                /* Loops through the `notes` array and renders a `Note` component for each item. 
                   - `note`: The individual note object passed as a prop to the `Note` component.
                   - `onDelete`: A function (deleteNote) passed as a prop to handle note deletion.
                   - `key`: A unique identifier (`note.id`) to help React efficiently render the list.
                */
            ))}
        </div>
        <h2> Create a Note</h2> {/* A header to indicate the note creation form. */}
        <form onSubmit={createNote}> {/* The form handles user input and submission. */}
            
            <label htmlFor="title">Title:</label> {/* Label to describe the title field */}
            <br /> {/* Line break for spacing */}
            <input 
                type="text" // Specifies the input type as a text field.
                id="title" // Unique identifier for this input element (used with `label`'s `htmlFor` attribute).
                required // Makes this input field mandatory before the form can be submitted.
                onChange={(e) => setTitle(e.target.value)} // Updates the `title` state whenever the user types.
                value={title} // Binds the input field's value to the `title` state.
            />

            <label htmlFor="content">Content:</label> {/* Label for the content field */}
            <br /> {/* Line break for spacing */}
            <textarea 
                id="content" // Unique identifier for this textarea element.
                name="content" // Name of the input (can be used for form submission or accessibility).
                required // Makes this textarea mandatory before submission.
                value={content} // Binds the textarea's value to the `content` state.
                onChange={(e) => setContent(e.target.value)} // Updates the `content` state whenever the user types.
            ></textarea>
            <br /> {/* Line break for spacing */}

            <input type="submit" value="Submit" /> {/* A button to submit the form */}
        </form>
    </div>
    );
}

// Export the `Home` component for use in other parts of the application
export default Home;
