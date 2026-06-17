import json
import re

from model import client
from prompt import PROMPT_TEMPLATE
from parser import JDExtractor


def extract_details(jd):

    prompt = PROMPT_TEMPLATE.format(jd=jd)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    # Extract JSON block safely
    json_match = re.search(r"\{.*\}", result, re.DOTALL)

    if not json_match:
        raise ValueError("No valid JSON found in model response")

    json_text = json_match.group()

    data = json.loads(json_text)

    validated_output = JDExtractor(**data)

    return validated_output.model_dump()


if __name__ == "__main__":

    jd = """
    Looking for Python developer with 3 years experience in SQL and Machine Learning.
    Bachelor's degree required.
    """

    print(extract_details(jd))