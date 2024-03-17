import React, { useState } from 'react';
import './CommonPages.css';

// You can create or import a loading spinner component
// For demonstration, I'll simply use "Loading..." text
const LoadingSpinner = () => < div className = "loading" > Loading... < /div>;

function HackersPage() {
    const [idea, setIdea] = useState('');
    const [results, setResults] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async(e) => {
        e.preventDefault();
        setIsLoading(true); // Start loading
        try {
            const response = await fetch('http://localhost:5000/process-idea', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ idea }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.statusText}`);
            }

            const data = await response.json();
            setResults(data); // Assuming the backend returns an array of similar projects
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setIsLoading(false); // End loading
        }
    };

    return ( <
        div className = "page-container" >
        <
        h1 className = "page-title" > For Hackers < /h1>

        { isLoading && < LoadingSpinner / > }

        {
            !isLoading && results.length > 0 && ( <
                div className = "table-scroll-container" >
                <
                table className = "table" >
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
                    results.map((project, index) => ( <
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
                /table> <
                /div>
            )
        }

        <
        form onSubmit = { handleSubmit }
        className = "chat-input-container" >
        <
        input type = "text"
        className = "chat-input"
        placeholder = "Enter your idea here....."
        value = { idea }
        onChange = {
            (e) => setIdea(e.target.value) }
        /> <
        button type = "submit"
        className = "chat-enter-btn" > { '>' } < /button> <
        /form> <
        /div>
    );
}

export default HackersPage;