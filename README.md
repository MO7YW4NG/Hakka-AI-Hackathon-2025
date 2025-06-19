# Hakka-AI-Hackathon-2025

This project provides a modular Python client for testing and interacting with the Hakka AI Hackathon 2025 APIs, including TTS (Text-to-Speech), ASR (Automatic Speech Recognition: file and real-time), and Translation services.

## Features
- Modular API clients for:
  - TTS (Text-to-Speech)
  - ASR File (File-based Speech Recognition)
  - ASR Real-time (WebSocket Speech Recognition)
  - Translation
- Easy configuration via `.env` file
- Example main script to demonstrate login, basic API calls, and logout
- WebSocket support for real-time ASR

## Setup
1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Copy `.env.template` to `.env`** and fill in your credentials and API URLs:
   ```sh
   cp .env.template .env
   # Then edit .env with your values
   ```

## Usage
Run the main script to test the APIs:
```sh
python main.py
```

### Real-time ASR WebSocket Example
To use the real-time ASR client:
```python
from asr_realtime_api import ASRRealtimeApi
import os

api = ASRRealtimeApi(os.getenv('ASR_HAKKA_REALTIME_BASE_URL'), os.getenv('USERNAME'), os.getenv('PASSWORD'))
api.login()
resp = api.get_streaming_access_info()
info = resp.json()['data'][0]
ws_url = info['url']
ticket = info['ticket']
# Connect with required parameters (e.g., type, rate)
api.connect_websocket(ws_url, ticket, type='raw', rate=16000)
```

## Project Structure
- `tts_api.py` — TTS API client
- `asr_file_api.py` — ASR File API client
- `asr_realtime_api.py` — ASR Real-time (WebSocket) API client
- `translate_api.py` — Translation API client
- `main.py` — Example script using all modules
- `requirements.txt` — Python dependencies
- `.env.template` — Example environment file

## Notes
- For the translation API, SSL verification is disabled by default due to a self-signed certificate.
- Use the provided `.env.template` to set up your `.env` file with valid credentials and API URLs.
- For real-time ASR, use the ticket and WebSocket URL from `get_streaming_access_info()`.

---
