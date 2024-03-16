
api_key = '<API-KEY>'

from openai import OpenAI
import re
client = OpenAI(api_key=api_key)

def check(prompt):
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a Hackathon Judge that can read the description that I give you and give me a list of keywords that would be useful to find other super similar projects, so no common AI words, super specific stuff."},
        {"role": "user", "content": prompt}
    ]
    )

    
    keywords_message = completion.choices[0].message.content
    keywords_list = keywords_message.split(".")
    keywords_list = [re.sub(r'\d+\s*', '', keyword).strip() for keyword in keywords_list]


    return keywords_list


