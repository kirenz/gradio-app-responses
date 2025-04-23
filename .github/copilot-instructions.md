If you use OpenAI's API, always use the new responses API:

```python
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
```