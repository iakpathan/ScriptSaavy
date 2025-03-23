import requests
import json

# ✅ Define API URL for chat endpoint
API_URL = "http://127.0.0.1:5000/chat"

def chat_loop():
    print("Welcome to AI Chat! Type 'exit' to quit.\n")
    
    session_id = input("Enter session ID (or press Enter for default): ")
    if not session_id:
        session_id = "default"

    while True:
        # ✅ Get user input
        message = input("You: ")

        # ✅ Exit condition
        if message.lower() == "exit":
            print("Goodbye!")
            break

        # ✅ Prepare request payload
        payload = {
            "message": message,
            "session_id": session_id
        }

        # ✅ Send POST request to Flask API
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                result = response.json()
                print(f"AI: {result['response']}\n")
            else:
                print(f"Error: {response.json().get('error', 'Unknown error')}")
        except Exception as e:
            print(f"Failed to connect to API: {str(e)}")


if __name__ == "__main__":
    chat_loop()
