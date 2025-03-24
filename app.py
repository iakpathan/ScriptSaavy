from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from agents.script_generator import generate_script, chat_with_memory
from utils.exporter import export_script
from chains.chains import get_chain_and_generate
from utils.tts_generator import generate_voiceover
from dotenv import load_dotenv

import os
import sys
import codecs

# ✅ Load environment variables
load_dotenv()

# ✅ Set default encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)

app = Flask(__name__)
CORS(app)

# ✅ Define directories
VOICEOVER_DIR = "voiceover"
SCRIPT_DIR = "scripts"

# ✅ Create directories if they don't exist
os.makedirs(VOICEOVER_DIR, exist_ok=True)
os.makedirs(SCRIPT_DIR, exist_ok=True)

@app.route('/')
def home():
    """Welcome message for the API."""
    return "Welcome to the AI Script Generator API! Use /generate or /chat endpoint."

@app.route('/generate', methods=['POST'])
def generate():
    """Generate a script and optional voiceover."""
    data = request.json
    topic = data.get('topic', '')
    language = data.get('language', 'en')
    format_type = data.get('format', 'pdf')
    duration = int(data.get('duration', 5))
    session_id = data.get("session_id", "default")

    if not topic:
        return jsonify({"error": "Topic is required!"}), 400

    try:
        # ✅ Generate the script with contextual memory
        script_content = generate_script(topic, duration, language, session_id)

        # ✅ Export script to desired format (PDF or other formats)
        export_path = export_script(script_content, format_type)
        script_filename = os.path.basename(export_path)

        # ✅ Generate voiceover if applicable
        audio_path = generate_voiceover(script_content, language, VOICEOVER_DIR)
        audio_filename = os.path.basename(audio_path)

        # ✅ Return generated script, export path, and audio path
        return jsonify({
            "script": script_content,
            "export_path": f"/download/{script_filename}",
            "audio_path": f"/download/{audio_filename}"
        }), 200, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as e:
        return jsonify({"error": f"Failed to generate script: {str(e)}"}), 500

@app.route('/download/<path:filename>', methods=['GET'])
def download_script(filename):
    """Download the generated script or audio."""
    if filename.endswith(".pdf") or filename.endswith(".txt"):
        directory = SCRIPT_DIR
    else:
        directory = VOICEOVER_DIR

    try:
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": f"Failed to download file: {str(e)}"}), 500

if __name__ == '__main__':
    # ✅ Ensure directories exist before running the app
    app.run(host='0.0.0.0', port=5000, debug=True)
