# Coding Standards & Best Practices

## General Guidelines

- Keep code simple and readable
- Use meaningful variable and function names
- Follow PEP 8 style guide for Python code
- Add appropriate error handling
- Assume the reader has no prior knowledge of the code
- Use comments and docstrings to explain complex logic
- Assume the .env file containing API keys is in the script's directory (don't override the .env file)

## OpenAI API Integration

When using OpenAI's API, implement the new responses format with the model gpt-4.1-nano and use dotenv for environment variables:

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
```

## Security Considerations
- Never hardcode API keys (use dotenv)
- Use environment variables for sensitive data
- Validate user inputs
