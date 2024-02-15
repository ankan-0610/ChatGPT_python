# ChatGPT API Conversation Program

This Python program utilizes the OpenAI GPT-3.5 Turbo model to create a conversational chatbot. The program takes user input, sends it to the ChatGPT API, and returns the assistant's response. The conversation continues until the user inputs "stop."

## Prerequisites

- Python 3.x
- OpenAI API key

## Getting Started

1. **Install dependencies:**

   ```bash
   pip install openai
   
2. **Set up your OpenAI API key:**

   Retrieve your OpenAI API key and set it as an environment variable. For example:

    ```bash
    export OPENAI_API_KEY="your_api_key_here"
3. **Run the program:**

    ```bash
    python chatbot.py
    
**Configuration**
    The chatbot.py script uses the gpt-3.5-turbo model by default. You can customize the model or other parameters by modifying the script.
**Usage**
    Enter your messages in the console, and the chatbot will respond accordingly.
    To end the conversation, type "stop."
    
**Important Notes**
    Ensure your OpenAI API key is kept secure and not shared publicly.
    Keep your environment variables, especially the API key, confidential.
    
**Contributing**
    Contributions are welcome. Feel free to open issues or pull requests.
