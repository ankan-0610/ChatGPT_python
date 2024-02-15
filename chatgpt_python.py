import openai
import os

# Set your OpenAI API key
api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = api_key

def chat_with_gpt(prompt, chat_history=[]):
    # Prepare the conversation history
    conversation = [{'role': 'system', 'content': 'You are a helpful assistant.'}]
    for idx, message in enumerate(chat_history):
        role = 'user' if idx % 2 == 0 else 'assistant'
        conversation.append({'role': role, 'content': message})

    # Add the current user input to the conversation
    conversation.append({'role': 'user', 'content': prompt})

    # Generate a response using the ChatGPT API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    # Extract and return the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply

# Start the conversation
user_input = ""
history = []

while user_input.lower() != "stop":
    user_input = input("You: ")
    
    # Check if the user wants to stop
    if user_input.lower() == "stop":
        break
    
    # Get assistant's response
    response = chat_with_gpt(user_input, history)
    
    # Display assistant's response
    print("Assistant:", response)
    
    # Update conversation history
    history.extend([user_input, response])
