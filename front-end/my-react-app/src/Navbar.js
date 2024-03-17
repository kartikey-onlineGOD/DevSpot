// Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';
import logo from './Assets/logo.png'; // Ensure the path to your logo is correct
import './Navbar.css'; // We'll create this CSS file next

function Navbar() {
    return ( <
        nav className = "navbar" >
        <
        Link to = "/"
        className = "navbar-logo" >
        <
        img src = { logo }
        alt = "DevSpot" / >
        DevSpot <
        /Link> <
        div className = "navbar-links" >
        <
        Link to = "/organizers"
        className = "nav-link" > For Organizers < /Link> <
        Link to = "/hackers"
        className = "nav-link" > For Hackers < /Link> <
        Link to = "/about"
        className = "nav-link" > About Us < /Link> <
        /div> <
        /nav>
    );
}

export default Navbar;