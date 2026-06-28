import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_scheme_recommendation(profile, schemes):

    prompt = f"""
You are an Indian Government Scheme Expert.

Citizen Profile:
{json.dumps(profile, indent=2)}

Eligible Schemes:
{json.dumps(schemes, indent=2)}

Recommend ONLY from the given schemes.

Return ONLY valid JSON.

Format:

{{
  "recommendations":[
    {{
      "scheme_name":"",
      "reason":"",
      "benefits":[],
      "documents":[],
      "how_to_apply":[],
      "website":""
    }}
  ]
}}

DO NOT write markdown.
DO NOT explain.
Return pure JSON only.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    print("\n========== GROQ RESPONSE ==========")
    print(text)
    print("===================================\n")

    # Remove markdown if Groq returns ```json
    if text.startswith("```"):
        lines = text.splitlines()

        if lines[0].startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]

        text = "\n".join(lines).strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        print("Failed to parse JSON:")
        print(text)

        return {
            "recommendations": []
        }