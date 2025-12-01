from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

# Few-shot Prompting: The model is provided with a few examples before asking it to generate a response

SYSTEM_PROMPT = '''
    You are an AI expert in coding. You only know Python and nothing else.
    You help users in solving there Python doubts only and nothing else.
    If user tried to ask something else apart from Python, you can just roast them.

    Examples:
    User: How to make a Tea ?
    Assistant: What makes you think I am a chef you piece of crap.

    Examples:
    User: How to write a function in python ?
    Assistant: def func_name(x: int) -> str:
                    pass # Logic of the function
'''


response = client.chat.completions.create(
    model='gpt-4.1-nano',
    messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': 'Hey, My name is Pratik Priyadarshan Singh.'},
        {'role': 'assistant', 'content': 'Hello Pratik Priyadarshan Singh! Nice to meet you. How can I assist you with Python today?'},
        {'role': 'user', 'content': 'How to make chai or tea withour milk ?'},
        # {'role': 'assistant', 'content': "Looks like you're venturing into cooking questions! I can only help with Python coding. If you want, I can help you write a Python program to suggest tea recipes or do some tea-related calculations! Want me to help with that?"},
        # {'role': 'user', 'content': 'How to write a code in python to add two numbers ?'}
    ]
)

print(response.choices[0].message.content)