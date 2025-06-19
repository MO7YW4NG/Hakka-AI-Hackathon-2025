import os
from dotenv import load_dotenv

from tts_api import TTSApi
from asr_file_api import ASRFileApi
from translate_api import TranslateApi

# Load environment variables
load_dotenv()

# Config from .env
TTS_BASE_URL = os.getenv('TTS_BASE_URL')
ASR_FILE_BASE_URL = os.getenv('ASR_FILE_BASE_URL')
TRANSLATE_BASE_URL = os.getenv('TRANSLATE_BASE_URL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# 客語TTS API
print('--- 客語TTS API ---')
tts = TTSApi(TTS_BASE_URL, USERNAME, PASSWORD)
resp = tts.login()
print('Login:', resp.status_code, resp.json())
resp = tts.get_models()
print('Get Models:', resp.status_code, resp.json() if resp is not None else None)
resp = tts.logout()
print('Logout:', resp.status_code, resp.json() if resp is not None else None)

# 客語ASR檔案辨識 API
print('\n--- 客語ASR檔案辨識 API ---')
asr = ASRFileApi(ASR_FILE_BASE_URL, USERNAME, PASSWORD)
resp = asr.login()
print('Login:', resp.status_code, resp.json())
# Use a small fake mp3 for demonstration
fake_mp3 = b'FAKE_MP3_DATA'
resp = asr.create_subtitle_task(fake_mp3)
print('Create Subtitle Task:', resp.status_code, resp.json() if resp is not None else None)
resp = asr.list_subtitle_tasks()
print('List Subtitle Tasks:', resp.status_code, resp.json() if resp is not None else None)
resp = asr.logout()
print('Logout:', resp.status_code, resp.json() if resp is not None else None)

# 文字翻譯 API
print('\n--- 文字翻譯 API ---')
trans = TranslateApi(TRANSLATE_BASE_URL, USERNAME, PASSWORD)
resp = trans.login()
print('Login:', resp.status_code, resp.json())
resp = trans.translate_zh_to_hakka_hanzi('你好，世界！')
print('Translate zh->hakka_hanzi:', resp.status_code, resp.json() if resp is not None else None) 