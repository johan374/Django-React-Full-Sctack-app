import { useState } from "react"; // Import React's useState hook for state management.
import api from "../api"; // Import the `api` module, which handles HTTP requests.
import { useNavigate } from "react-router-dom"; // Import the `useNavigate` hook for navigation.
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants"; // Import constants for token keys.
import "../styles/Form.css" // Import the CSS styles for this component.
import LoadingIndicator from "./LoadingIndicator"; // Import the LoadingIndicator component to show during loading.

function Form({ route, method }) {
    const [username, setUsername] = useState(""); // State to hold the username entered in the form.
    const [password, setPassword] = useState(""); // State to hold the password entered in the form.
    const [loading, SetLoading] = useState(false); // State to handle the loading state of the form submission.

    const navigate = useNavigate(); // Hook for navigating to other pages, useful for redirection.

    const name = method === "login" ? "Login" : "Register"; // Determines the button text based on the `method` prop (either "Login" or "Register").

    const handleSubmit = async (e) => { // Function to handle the form submission when the button is clicked.
        console.log("Form submitted", { route, method }); // Log form submission details to the console.
        SetLoading(true); // Set the loading state to true when the form is being submitted.
        e.preventDefault(); // Prevent the default form submission behavior.

        try {
            console.log("Sending registration request"); // Log to indicate that a request is being sent.
            const res = await api.post(route, { username, password }); // Make an HTTP POST request to the server with the provided `username` and `password`.
            console.log("Registration response:", res); // Log the response from the server.

            if (method === "login") { // If the method is "login", save the tokens to local storage and navigate to the home page.
                localStorage.setItem(ACCESS_TOKEN, res.data.access); // Save access token to local storage.
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh); // Save refresh token to local storage.
                navigate("/"); // Redirect to the home page.
            } else { // If the method is "register", navigate to the login page.
                console.log("Navigating to login");
                navigate("/login"); // Redirect to the login page after registration.
            }
        } catch (error) { // Catch any errors that occur during the request.
            console.error("Full error:", error); // Log the full error to the console.
            console.error("Error response:", error.response); // Log the error response for debugging.
            alert(error.response // If an error response exists, show it as an alert, otherwise show a generic failure message.
                ? JSON.stringify(error.response.data) 
                : "Registration failed"
            );
        } finally {
            SetLoading(false); // Set loading to false once the request is complete, regardless of success or failure.
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container"> {/* Form element that triggers `handleSubmit` when submitted */}
            <h1>{name}</h1> {/* Display the form title (Login or Register). */}
            <input
                className="form-input" // CSS class for styling.
                type="text" // Input type: text for the username.
                value={username} // Bind the input's value to the `username` state.
                onChange={(e) => setUsername(e.target.value)} // Update the state on input change.
                placeholder="Username" // Placeholder text for the username field.
            />
            <input
                className="form-input" // CSS class for styling.
                type="password" // Input type: password for the password field.
                value={password} // Bind the input's value to the `password` state.
                onChange={(e) => setPassword(e.target.value)} // Update the state on input change.
                placeholder="Password" // Placeholder text for the password field.
            />
            {loading && <LoadingIndicator />} {/* If the form is loading, show the LoadingIndicator component. */}
            <button
                className="form-button" // CSS class for styling.
                type="submit" // Button type: submit to trigger form submission.
                disabled={loading} // Disable the button when the form is loading.
            >
                {loading ? "Loading..." : name} {/* Display "Loading..." when submitting; otherwise, the name (Login/Register). */}
            </button>
        </form>
    );
}

export default Form; // Export the component to be used elsewhere.
