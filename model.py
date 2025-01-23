from together import Together
from helper import get_together_api_key
from redlines import Redlines
from IPython.display import Markdown, display

def get_completion(prompt):
    client = Together(api_key=get_together_api_key())

    output = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    response_content = output.choices[0].message.content
    return response_content


def process_text(original_text):
    prompt = f"""proofread and correct this text: ```{original_text}``` 
        instructions:
        - correct any spelling or grammar mistakes
        - make sure the text is clear and easy to read
        - return only the corected version without any additional comments or suggestions"""
    response = get_completion(prompt)

    diff = Redlines(original_text, response)
    return diff.output_markdown