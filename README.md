 # 🎥 Saavy Script AI

Saavy Script AI is a web application that allows content creators to **generate YouTube scripts and voiceovers automatically** by simply entering a topic. It uses AI to generate the script, converts it into a downloadable PDF, and also generates an MP3 voiceover using text-to-speech.

---
 

## 🌟 Features


- 🎯 Generate high-quality scripts for YouTube, Podcasts, and LinkedIn
- 🧠 AI memory to remember past chats
- 📁 Export scripts in PDF format
- 🎙️ Text-to-speech voiceover generation (english)
- 🔥 Trending topic analysis and search
- 🖥️ Clean and responsive user interface (HTML + CSS + JS)
- 🚀 Fast LLM responses using Groq API and LangChain


---

## 🧪 Tech Stack

- **Frontend**: HTML, CSS (in `templates/`)
- **Backend**: Python (Flask)
- **AI Layer**: LangChain, Groq API
- **Utilities**: PyPDF2, gTTS, OS, dotenv
- **Project Structure**: Modular design for maintainability

---

## ⚙️ Pre-Installation Setup

### 🐍 Python & Pip

Install Python and pip (skip if already installed):

```bash
 # 1. Clone the repository
git clone https://github.com/iakpathan/ScriptSaavy.git
cd ScriptSaavy

# 2. Create and activate a virtual environment
pip install virtualenv
virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key to .env
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 5. Run the Flask app
python app.py
📁 Outputs and UI Features
The scripts/ folder inside Script/ stores generated output (PDF/voice).

The UI has buttons to download:
PDF (generated_script.pdf)
MP3 voiceover file

📂 Project Structure
bash
Copy
Edit
saavy-script-ai/
├── Script/                    # Custom modules or notebooks (WIP)
├── agents/                   # LangChain agents
├── chains/                   # LLM chain configuration and classifier
├── data/                     # Input/output data (if any)
├── exports/                  # Exported PDFs or logs
├── templates/                # Frontend HTML templates
├── tests/                    # Test scripts (unit/integration)
├── utils/                    # Utility functions (PDF, TTS)
├── voiceover/                # Output voiceover files
├── app.py                    # Main Flask backend
├── chat_cli.py               # Command-line chatbot version
├── generated_script.pdf      # Sample output
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
├── README.md                 # Project documentation
🚀 Run Locally
 

🔗 API Endpoints
Route	Method	Description
/	GET	Home page
/generate	POST	Generate script and voiceover
/chat	POST	Chatbot conversation
/download/<fn>	GET	Download audio file

📤 Output Files
PDF files are saved in: Script/scripts/generated_script.pdf

Voiceover files are saved in: voiceover/generated_voice.mp3

You can download both directly from the UI after generation.

📄 License
Licensed under the MIT License. See LICENSE for details.

📬 Contact
👤 Maintainers & developers: iakpathan and team.

