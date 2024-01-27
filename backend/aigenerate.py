import openai
import json

# Set your OpenAI GPT-3 API key
openai.api_key = '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'

#prompt = "Give me a question about water that elementary school kids should know."

# Make a request to the GPT-3 Chat API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Give me a question and the answer about water that elementary school kids should know with multiple choice answers."}
    ]
)

# Print the generated response
json_response = response['choices'][0]['message']['content']
print(json.dumps(json_response, indent=2))

