from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_response(message):
    response = client.responses.create(
        model="gpt-4.1-nano",
        input=message
    )
    return response.output_text

demo = gr.Interface(
    fn=get_response,
    inputs="text",
    outputs="text",
    title="This is my Chatbot",
    description="Enter your message and get a response from the Chatbot"
)

if __name__ == "__main__":
    demo.launch()
