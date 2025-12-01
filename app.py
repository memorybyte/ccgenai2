from dotenv import load_dotenv

from google import genai
from openai import OpenAI

load_dotenv()


## GEMINI:
# The client gets the API key from the environment variable `GEMINI_API_KEY`
gemini_client = genai.Client()

response = gemini_client.models.generate_content(
    model='gemini-2.5-flash',
    contents=['What is the population of India in 2025 November ?']
)

print(response.text)


## OPENAI:
openai_client = OpenAI()

response = openai_client.responses.create(
    model='gpt-4.1-nano',
    input='What is the population of India in 2025 November ?'
)

print(response.output_text)



## Installation

# pip install python-dotenv

# pip install tiktoken

# pip install openai
# pip install google-genai

# 01 Introduction: 
# Tokenization:
# Vocabulary: mapping
# Vocab Size:
# Vector Embeddings
# Positional Encoding
# Self Attention
# Multi-head Attention


# 02: Prompting Techniques
# Style: Alpaca Prompt, ChatML, INST Format

# 03


# 04


# 05


# 06


# 07


# 08


# 09


# 10


# 11


# 12


# 13


# 14
