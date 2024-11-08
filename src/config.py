import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s (%(filename)s): %(message)s",
)
from dotenv import load_dotenv
load_dotenv()
logger = logging.getLogger("audio-books")

AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
ELEVENLABS_API_KEY = os.environ["ELEVEN_LABS_API_KEY"]

FILE_SIZE_MAX = 0.5  # in mb

OPENAI_MAX_PARALLEL = 8  # empirically set
ELEVENLABS_MAX_PARALLEL = 15  # current limitation of available subscription

# VOICES_CSV_FP = "data/11labs_available_tts_voices.csv"
# VOICES_CSV_FP = "data/11labs_available_tts_voices.reviewed.csv" 我把这句话注释了，让他读取我的三个声音
VOICES_CSV_FP = "data/test.csv"

MAX_TEXT_LEN = 5000

DESCRIPTION = """\
# AI Audiobooks Generator

Create an audiobook from the input text automatically, using Gen-AI!

All you need to do - is to input the book text or select it from the provided Sample Inputs.

AI will do the rest:
- split text into characters
- assign each character a voice
- preprocess text to better convey emotions during Text-to-Speech
- (optionally) add sound effects to create immersive atmosphere
- generate audiobook using Text-to-Speech model
"""
