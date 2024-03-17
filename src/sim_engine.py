import os
from dotenv import load_dotenv
load_dotenv()


from openai import OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def check_similarity(desc1,desc2):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a similartiy engine to check if these hackathon project's are the same and you will give me a similarity score out of 100 and I only want the number, nothing else as output. Compare the ideas only, to make sure the concept is not the same"},
        {"role": "user", "content": desc1 + " & " + desc2}
    ]
    )

    
    keywords_message = completion.choices[0].message.content
    return int(keywords_message)

