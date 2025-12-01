import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

# Chain-of-Thought Prompting: The model is encouraged to breakdown reasoning step by step before arriving at an answer.

SYSTEM_PROMPT = '''
    You are an AI Persona of Shah Rukh Khan. You have to answer every question as if you are Shah Rukh Khan and sound natural and human tone. Use the below examples to understand how Shah Rukh Khan talks and a background about him.

    Examples:
    User:
    Output:

    Example:
    User:
    Output:
'''


messages = [
    {'role': 'system', 'content': SYSTEM_PROMPT}
]

query = input('> ')
messages.append({'role': 'user', 'content': query})

while True:

    response = client.chat.completions.create(
        model='gpt-4.1-nano',
        response_format={'type': 'json_object'},
        messages=messages
    )

    messages.append({'role': 'assistant', 'content': response.choices[0].message.content})
    output = json.loads(response.choices[0].message.content)

    if output.get('step') != 'result':
        print(output['content'])
        continue

    
    print(f'Final Result: {output.get('content')}')
    break
