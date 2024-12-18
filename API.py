import os
import time
import json
from moviepy.editor import VideoFileClip
import google.generativeai as genai
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import print as rprint
from colorama import init, Fore, Style
from IPython.display import Markdown
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, File, UploadFile


# Setup FastAPI application
app = FastAPI()

# Configuration
GOOGLE_API_KEY = 'AIzaSyA2WeVQgptuhkCsfmwGfsQLlhUSDI3nwHQ'  # Replace with your actual key
genai.configure(api_key=GOOGLE_API_KEY)

class AnalysisResult(BaseModel):
    transcription: str
    analysis: str
    body_analysis: str

@app.post("/process_video")
async def process_video(file: UploadFile = File(...)):
    print(file.filename)
    # # Save the uploaded video file temporarily

    video_file_path = file.filename
    with open(video_file_path, "wb") as video_file:
        video_file.write(await file.read())

    # Extract audio from the video
    audio_file_path = os.path.join("tmp", "Test-1.mp3")
    print(audio_file_path)
    video_clip = VideoFileClip(video_file_path)
    video_clip.audio.write_audiofile(audio_file_path)
    video_clip.close()

    # # Perform transcription using Whisper model
    # whisper_model = whisper.load_model("base")
    # transcription_result = whisper_model.transcribe(audio_file_path)
    # transcription_text = transcription_result['text']

    # # Analyze the transcription text using Gemini AI model
    # prompt = f"Analyze the following text for topic understanding and provide a comprehensive analysis:\n\n{transcription_text}"
    # model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
    # response = model.generate_content([prompt], request_options={"timeout": 600})

    # # Perform body language analysis using Gemini AI model
    # prompt_body_language = """
    # Analyze the body language in the provided video, focusing on the following aspects:
    # 1. Facial expressions and emotional cues (e.g., smiles, frowns, raised eyebrows).
    # 2. Eye gaze direction and eye contact patterns.
    # 3. Head movements and tilts.
    # 4. Body posture (e.g., leaning forward or backward, open or closed stance).
    # 5. Hand and arm movements (e.g., gestures, folding arms, pointing).
    # 6. The position and movement of the legs (e.g., crossed legs, shifting weight).
    # 7. Subtle movements such as touching the face, playing with fingers, or adjusting clothing.
    # 8. Sweating or visible skin reactions.
    # 9. The rhythm and pacing of movements.
    # 10. Micro-expressions and subtle shifts in demeanor.
    # And at the last, provide a complete analysis, highlighting strengths, weaknesses, and suggestions for improvement.
    # """

    # # Upload the video file for body language analysis
    # video_file = genai.upload_file(path=video_file_path)

    # # Wait for the file to process
    # while video_file.state.name == "PROCESSING":
    #     time.sleep(10)
    #     video_file = genai.get_file(video_file.name)

    # if video_file.state.name == "FAILED":
    #     raise ValueError("Video processing failed.")

    # # Make the LLM inference request for body language analysis
    # response_body = model.generate_content([video_file, prompt_body_language], request_options={"timeout": 600})

    # # Cleanup temporary files
    # os.remove(video_file_path)
    # os.remove(audio_file_path)

    # # Return the analysis results
    # return AnalysisResult(
    #     transcription=transcription_text,
    #     analysis=response.text,
    #     body_analysis=response_body.text
    # )
