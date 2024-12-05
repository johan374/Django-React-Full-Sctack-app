// Import required libraries and components.
import React from 'react'; // React library for building UI components.
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'; 
// BrowserRouter enables navigation between different pages in a React app.
// Routes is used to define all the routes of the application.
// Route defines individual routes.
// Navigate is used for programmatic navigation (redirects).

import Login from "./pages/Login"; // Login component for the login page.
import Register from './pages/Register'; // Register component for user registration.
import Home from './pages/Home'; // Home component for the main page after login.
import NotFound from './pages/NotFound'; // NotFound component to handle undefined routes.
import ProtectedRoute from './components/ProtectedRoute'; 
// ProtectedRoute component ensures only authenticated users can access certain pages.

// Logout component: clears local storage and redirects to the login page.
function Logout() {
  localStorage.clear(); // Clears all stored data (e.g., tokens) in localStorage.
  return <Navigate to="/login" />; // Redirects the user to the login page.
}

// RegisterAndLogout component: clears local storage and renders the Register page.
function RegisterAndLogout() {
  localStorage.clear(); // Clears all stored data in localStorage.
  return <Register />; // Renders the `Register` component.
}

// App component: sets up the routing structure of the application.
function App() {
  return (
    <BrowserRouter>
      {/* Wrap the app with BrowserRouter to enable routing. */}
      <Routes>
        {/* Define the application routes. */}
        
        <Route
          path='/'
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        {/* '/' route (home page): Only accessible to authenticated users.
            - Wrapped inside `ProtectedRoute`.
            - If authenticated, renders the `Home` component.
            - If not authenticated, redirects to the login page. */}

        <Route path='/login' element={<Login />} />
        {/* '/login' route: Displays the `Login` component. */}

        <Route path='/logout' element={<Logout />} />
        
        <Route path='/register' element={<RegisterAndLogout />} />
        {/* '/register' route: Clears localStorage and displays the `Register` component. */}
        
        <Route path='*' element={<NotFound />} />
        {/* Catch-all route: Handles undefined paths.
            - Displays the `NotFound` component.
            - Helps provide feedback when a user navigates to an invalid URL. */}
      </Routes>
    </BrowserRouter>
  );
  // End of the routing setup.
}

export default App;
// Exports the `App` component to make it available for rendering in the main entry point of the app (e.g., index.js).
