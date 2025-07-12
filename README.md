# ADK Codebreaker Agent
A simple AI agent built with Google's Agent Development Kit (ADK) that can decrypt messages, inspired by the codebreakers of Bletchley Park.

This project was created for the Google's Agent Development Kit introductory workshop for the event "Build with AI" at GDG Bletchley Park.

## 🚀 Features
- Simple & Educational: A clear, easy-to-understand example of a multi-tool AI agent.
- Multi-Tool Logic: Demonstrates how an agent can use one tool to get information (a key) and pass it to another tool to perform an action (decrypt a message).
- Enigma themed: The agent is styled as a "codebreaker" with a bit of personality in its responses. Because we are at Bletchley Park!
- Built with Google's ADK: A great starting point for anyone looking to learn the fundamentals of the Agent Development Kit.

## 🛠️ Getting Started
To run this agent on your local machine, follow these steps.

### Prerequisites
Create a new Python virtual environment (note: Python 3.11 is preferred, otherwise you should use the --ignore-requires-python parameter in pip3 install):

Google Cloud SDK installed and authenticated.

### Installation & Running
1. Create & Activate Virtual Environment (Recommended):
```shell
# Create
python -m venv .venv
# Activate (each new terminal)
# macOS/Linux: source .venv/bin/activate
# Windows CMD: .venv\Scripts\activate.bat
# Windows PowerShell: .venv\Scripts\Activate.ps1
```  
2. Install the ADK:
```shell
pip install google-adk
```
3. Install the Google Cloud CLI: https://cloud.google.com/sdk/docs/install
4. Run and follow the instructions:
```shell
gcloud init
```
5. Get an API key from Google AI Studio.
6. Open the .env file located inside (enigma_cracker/) and copy-paste the following code.
```shell
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=PASTE_YOUR_ACTUAL_API_KEY_HERE
```
7. Run the web interface:
- Navigate to the directory that contains the enigma_cracker folder.
- Run the following command:
```shell
adk web
```
- Open http://127.0.0.1:8000 in your browser.
8. Test the agent:
- Write an encrypted message, like: KHOOR

## 🕵️‍♂️ How It Works
The cracker_agent has a simple, three-step mission:

1. It calls the get_daily_setting tool to get the secret decryption key (which is hardcoded to 3).
2. It then calls the decrypt_message tool, passing it the user's message and the key it just retrieved.
3. Finally, it presents the decrypted message back to the user!
