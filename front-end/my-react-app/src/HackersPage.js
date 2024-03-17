// HackersPage.js
import React from 'react';
import './CommonPages.css'; // Ensure the path is correct, assuming you're using the same styles as OrganizersPage

function HackersPage() {
    return ( <
        div className = "page-container" >
        <
        h1 className = "page-title" > For Hackers < /h1> <
        div className = "chat-container" >
        <
        input type = "text"
        className = "chat-input"
        placeholder = "Type your idea..." / >
        <
        button className = "chat-enter-btn" > > < /button> < /
        div > <
        /div>
    );
}

export default HackersPage;