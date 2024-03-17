import React, { useState } from 'react';
import './CommonPages.css';

function OrganizersPage() {
    const [projectLink, setProjectLink] = useState('');
    const [similarProjects, setSimilarProjects] = useState([]);

    const handleSubmit = async(e) => {
        e.preventDefault(); // Prevents the default form submission behavior
        try {
            // Assuming your backend endpoint for processing the project link is '/find-similar'
            const response = await fetch('http://localhost:5000/find-similar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ projectLink }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const data = await response.json();
            setSimilarProjects(data); // Assuming the backend returns an array of similar projects
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return ( <
        div className = "page-container" >
        <
        h1 className = "page-title" > For Organizers < /h1> <
        form onSubmit = { handleSubmit }
        className = "form-container" >
        <
        input type = "text"
        className = "chat-input"
        placeholder = "Paste the project link here..."
        value = { projectLink }
        onChange = {
            (e) => setProjectLink(e.target.value) }
        /> <
        button type = "submit"
        className = "chat-enter-btn" > { '>' } < /button> <
        /form> {
            similarProjects.length > 0 && ( <
                table >
                <
                thead >
                <
                tr >
                <
                th > Project Name < /th> <
                th > Link < /th> <
                th > Similarity Score < /th> <
                /tr> <
                /thead> <
                tbody > {
                    similarProjects.map((project, index) => ( <
                        tr key = { index } >
                        <
                        td > { project.name } < /td> <
                        td > < a href = { project.link }
                        target = "_blank"
                        rel = "noopener noreferrer" > { project.link } < /a></td >
                        <
                        td > { project.similarity } % < /td> <
                        /tr>
                    ))
                } <
                /tbody> <
                /table>
            )
        } <
        /div>
    );
}

export default OrganizersPage;