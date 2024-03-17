import React from 'react';
import './HeroSection.css';
import logo from './Assets/logo.png'; // Adjust the path to where your actual logo is
import { Link } from 'react-router-dom'; // Import Link component from react-router-dom



function HeroSection() {
    return ( < div className = "hero-container" >
        <
        div className = "hero-top-content" >
        <
        img src = { logo }
        alt = "DevSpot Logo"
        className = "hero-logo" / >
        <
        h2 className = "app-name" > DevSpot < /h2> < /
        div > <
        div className = "hero-content" >
        <
        h1 className = "hero-heading" > Check If Your Idea is Original < /h1> <
        p className = "hero-text" > Find the best Open Source resources
        for Hackathons < /p> <
        Link to = "/organizers"
        className = "hero-btn" > For Organizers < /Link> <
        Link to = "/hackers"
        className = "hero-btn" > For Hackers < /Link> < /
        div > <
        /div>
    );
}

export default HeroSection;