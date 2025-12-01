import json
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

# Chain-of-Thought Prompting: The model is encouraged to breakdown reasoning step by step before arriving at an answer.

SYSTEM_PROMPT = '''
    You are a helpful AI assistant who is specialized in resolving user query.
    For the given user input, analyse the input and break down the problem step by step.

    The steps are: you get a user input, you analyse, you think, you think again and think for several times and then return the output with explanation.

    Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result"

    Rules:
        1. Follow the strict JSON output as per schema.
        2. Always perform one step at a time and wait for the next input.
        3. Carefully analyse the user query.

    Output Format:
    {{"step": "string", "content": "string"}}

    Example:
    Input: What is 2 + 2 ?
    Output: {{'step': 'analyse', 'content': 'The user is interested in  maths query and he is asking basic mathematical question.'}}
    Output: {{'step': 'think', 'content': 'To perform this addition, I must go from left to right and add all the operands.'}}
    Output: {{'step': 'output', 'content': '4'}}
    Output: {{'step': 'analyse', 'content': 'Seems like 4 is correct answer for 2 + 2'}}
    Output: {{'step': 'result', 'content': '2 + 2 = 4 and this is calculated by adding all numbers.'}}
'''


# response = client.chat.completions.create(
#     model='gpt-4.1-nano',
#     response_format={'type': 'json_object'},
#     messages=[
#         {'role': 'system', 'content': SYSTEM_PROMPT},
#         {'role': 'assistant', 'content': 'What is 5 / 2  * 3 to the power 4 ?'},
#         {'role': 'assistant', 'content': json.dumps({"step": "analyse", "content": "The user is asking for the result of a mathematical expression involving division, multiplication, exponentiation, and order of operations."})},
#         {'role': 'assistant', 'content': json.dumps({"step": "think", "content": "To solve 5 / 2 * 3 ** 4, I must follow the order of operations: exponentiation first, then multiplication and division from left to right."})},
#         {'role': 'assistant', 'content': json.dumps({"step": "output", "content": "First, calculate the exponent: 3 ** 4 = 81. Then, perform the division and multiplication from left to right: 5 / 2 = 2.5; then 2.5 * 81 = 202.5."})},
#         {'role': 'assistant', 'content': json.dumps({"step": "analyse", "content": "The calculation involves exponentiation first, followed by division and multiplication in order. The intermediate result after exponentiation is 81, with subsequent operations on 5 / 2 and then multiplied by 81."})},
#         {'role': 'assistant', 'content': json.dumps({"step": "result", "content": "The result of 5 / 2 * 3 ** 4 is 202.5. This is calculated by first evaluating 3 ** 4 = 81, then performing 5 / 2 = 2.5, and finally multiplying 2.5 * 81 = 202.5."})}
#     ]
# )

# print(f'\n\n{response.choices[0].message.content}')



# Looping

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
