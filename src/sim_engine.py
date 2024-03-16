
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def check_similarity(prompt):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a similartiy engine to check if these hackathon project's are the same and you will give me a similarity score out of 100 and I only want the number, nothing else as output"},
        {"role": "user", "content": prompt}
    ]
    )

    
    keywords_message = completion.choices[0].message.content
    return int(keywords_message)

