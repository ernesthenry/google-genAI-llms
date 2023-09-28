import os
import google.generativeai as palm
from google.api_core import client_options as client_options_lib
from google.api_core import retry


palm.configure(
    api_key=get_api_key(),
    transport="rest",
    client_options=client_options_lib.ClientOptions(
        api_endpoint=os.getenv("GOOGLE_API_BASE"),
    )
)


for m in palm.list_models():
    print(f"name: {m.name}")
    print(f"description: {m.description}")
    print(f"generation methods:{m.supported_generation_methods}\n")


models = [m for m in palm.list_models() 
    if 'generateText' 
    in m.supported_generation_methods]
models

model_bison = models[0]
model_bison

@retry.Retry()
def generate_text(prompt,
                  model=model_bison,
                  temperature=0.0):
    return palm.generate_text(prompt=prompt,
                              model=model,
                              temperature=temperature)

prompt = "Show me how to iterate across a list in Python."
completion = generate_text(prompt)
print(completion.result)

prompt = "write code to iterate across a list in Python"
completion = generate_text(prompt)
print(completion.result)


# Modify the prompt with your own question
prompt = "Show me how to [...]"

completion = generate_text(prompt)