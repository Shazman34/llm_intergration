import requests

# Ollama local server URL
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"  # Change this to the model you prefer

def chat_with_ollama(prompt):
    """Sends user prompt to Ollama server and returns the response."""
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # Set to True if you want to stream responses
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()  # Raise error for bad responses
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("ChatGPT-Ollama (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        bot_response = chat_with_ollama(user_input)
        print(f"Ollama: {bot_response}\n")
