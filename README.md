# OpenAI Chat Assistant

A Python script that creates an interactive chat interface using OpenAI's GPT-3.5 Turbo model. The script maintains conversation history and displays token usage for each interaction.

## Features
- Interactive chat interface
- Token usage monitoring
- Easy exit with 'exit' or 'quit' commands

## Setup

1. Install required packages:
```bash
pip install openai python-dotenv
```

2. Create a `.env` file in the project directory with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the script:
```bash
python first_call.py
```

- Type your messages after the "User:" prompt
- Type 'exit' or 'quit' to end the conversation
- Each response will show the assistant's reply and token count

## Dependencies
- openai
- python-dotenv
- os (built-in)