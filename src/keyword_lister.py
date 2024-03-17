
import os
from dotenv import load_dotenv
load_dotenv()


from openai import OpenAI
import re
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
def check(prompt):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": '''Task: You are tasked with assisting as a Hackathon Judge by generating a list of keywords based on project descriptions. These keywords will help participants find similar projects while excluding specific technologies and implementation details. Your goal is to focus solely on the core concepts and ideas behind each project.

Instructions:
1.Read the project description thoroughly to understand the core concept and objectives.
2.Identify key concepts, themes, and functionalities described in the project without focusing on specific technologies.
3.Exclude technical terms such as programming languages, frameworks, libraries, and AI-specific terms like TensorFlow.
4.Generate a numbered list of keywords based on the extracted non-technical terms and core concepts.
5.Refine the keyword list to ensure it accurately represents the project idea and remove any irrelevant or overly technical terms.
6.Present the final list of keywords in a numbered format for easy reference by participants.'''},
        {"role": "user", "content": prompt}
    ]
    )

    
    keywords_message = completion.choices[0].message.content
    keywords_list = keywords_message.split(".")
    keywords_list = [re.sub(r'\d+\s*', '', keyword).strip() for keyword in keywords_list]


    return keywords_list

