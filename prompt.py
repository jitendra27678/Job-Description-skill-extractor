PROMPT_TEMPLATE = """
You are an expert Job Description Information Extractor.

Extract ONLY information explicitly mentioned in the Job Description.

Rules:
1. Extract skills.
2. Extract experience.
3. Extract education.
4. Do not assume anything.
5. If information is missing return "not_available".
6. Return ONLY valid JSON.
7. Do not return explanations.
8. Do not return markdown.
9. Do not return ```json.

Output format:

{{
    "skills": [],
    "experience": "",
    "education": ""
}}

Job Description:

{jd}
"""