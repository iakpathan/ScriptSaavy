from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import json
from oauth2client import file, client, tools

# Setup YouTube API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRET_FILE = "client_secrets.json"

def authenticate_youtube():
    """Authenticate and build YouTube API client."""
    store = file.Storage("token.json")
    creds = store.get()
    
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        creds = tools.run_flow(flow, store)
    
    return build("youtube", "v3", credentials=creds)

def upload_to_youtube(title, description, file_path, tags=[]):
    """Upload video or audio to YouTube."""
    try:
        youtube = authenticate_youtube()
        
        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": "22"  # Default: Category 22 (People & Blogs)
            },
            "status": {"privacyStatus": "public"}
        }
        
        # Upload file
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
        response = request.execute()
        
        return f"🎥 Successfully uploaded to YouTube! Video ID: {response['id']}"
    except Exception as e:
        return f"Error uploading to YouTube: {str(e)}"

