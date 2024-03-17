import React from 'react';
import './App.css';
import Navbar from './Navbar'; // Import the Navbar component
import HeroSection from './HeroSection';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import OrganizersPage from './OrganizersPage';
import HackersPage from './HackersPage';


function App() {
    return ( <
        Router >
        <
        div className = "App" >
        <
        Navbar / > { /* Include the Navbar component */ } <
        Routes >
        <
        Route path = "/"
        element = { < HeroSection / > }
        /> <
        Route path = "/organizers"
        element = { < OrganizersPage / > }
        /> <
        Route path = "/hackers"
        element = { < HackersPage / > }
        /> <
        /Routes> <
        /div> <
        /Router>
    );
}

export default App;