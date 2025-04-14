 # 🎥 Saavy Script AI

Saavy Script AI is a web application that allows content creators to **generate YouTube scripts and voiceovers automatically** by simply entering a topic. It uses AI to generate the script, converts it into a downloadable PDF, and also generates an MP3 voiceover using text-to-speech.

---

## 🛠 Features

- 🎯 Input a topic and instantly generate a content script.
- 📄 Download the script as a PDF.
- 🔊 Download the generated voiceover as an MP3.
- 📚 Maintains a search history on the sidebar.
- 🧹 Option to clear search history.
- 🤖 Backend powered by Flask + Groq API (ChatGPT-like model).

---


---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- pip
- A Groq API key (used to access Mixtral/LLM)
- Required Python packages (see below)

### 📦 Installation

 1.clone the repo:
 

2.Install dependencies:

pip install flask groq gtts
groq_api_key = "your_groq_api_key"

 
Add your Groq API key:
groq_api_key = "your_groq_api_key"
Open app.py and replace:




💻 Running the App
Start the Flask server:

python app.py
Open your browser and navigate to:
http://127.0.0.1:5000

🧪 Usage
Enter a topic in the input field.

Click on Generate.

Wait for the script and voiceover to be created.

Download the script (PDF) and voiceover (MP3) using the links.

View your past topics in the sidebar under Search History.


🧠 Powered By
Groq API

gTTS (Google Text-to-Speech)

Flask (Python web framework)

📌 Future Improvements
Add support for choosing voice type (male/female).

Allow selection of output languages.

Add login system for saving history per user.

Include video generation from script + voice.




Let me know if you want a `requirements.txt` file or want to publish it on GitHub



