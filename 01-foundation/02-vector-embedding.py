from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = 'Dog chases cat.'
response = client.embeddings.create(
    model='text-embedding-3-small',
    input=text
)

print(f'Response: {response}')
print(f'Embedded Vector: {response.data[0].embedding}')
print(f'Vector Length: {len(response.data[0].embedding)}')