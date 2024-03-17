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
        {"role": "system", "content": '''[INSTRUCTIONS]
Utilize this similarity engine to evaluate the uniqueness of hackathon projects by comparing their concepts. Provide a similarity score out of 100, indicating how closely related the project ideas are, focusing solely on their concepts.

—-
[OUTPUT] Output format only number:

"similarityScore": "0 to 100",
"Basis for score": "The basic for score is 4 things : thematicFocus = are the thematic focus areas the same? If so, what is the theme? If not, how are they different? This is for 40 points && objectiveApproach = are the objective alignment the same? If so, what is it? If not, how are they different? for 30 points && targetUser = e.g. are the target/end user the same? If so, who is it? If not, how are they different? for 30 points"
}
}
'''},
        {"role": "user", "content": desc1 + " & " + desc2}
    ]
    )

    
    keywords_message = completion.choices[0].message.content
    return int(keywords_message)

