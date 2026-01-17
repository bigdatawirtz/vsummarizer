import gradio as gr
import ffmpeg
import whisper
import torch
import requests
import os
from pytubefix import YouTube
from dotenv import load_dotenv

load_dotenv()
OLLAMA_HOST = os.getenv("OLLAMA_HOST")

audio_path = 'data/output.wav'

def download_video(url, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    
    yt = YouTube(url)
    
    # Get the best quality stream (combines video+audio)
    stream = yt.streams.get_highest_resolution()
    
    # Download to the specified directory
    video_path = stream.download(output_path=output_dir)
    
    return video_path

def extract_audio(video_path, output_audio_path):
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
    ffmpeg.input(video_path).output(output_audio_path).run(overwrite_output=True)


def transcribe_audio(audio_path):
    model = whisper.load_model("base").to(device)
    result = model.transcribe(audio_path)
    return result["text"]

# Define the function to summarize text using OLLAMA
def summarize_text(text):
    ollama_url = f"http://{OLLAMA_HOST}:11434/v1/chat/completions"  # Replace with your OLLAMA API URL
    headers = {"Content-Type": "application/json"}
    #data = {"text": text}
    
    data = {
        "model": "llama3.3",
        "messages": [
            {
                "role": "user",
                "content": f"Summarize this text: {text} in just a few lines."
            }
        ]
        } 
    
    response = requests.post(ollama_url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return "Error: Failed to summarize text"


# Define a function that takes a video file as input and returns a long text
def process_video(video_path):

    # Extract audio
    extract_audio(video_path, audio_path)

    # Perform speech recognition
    transcription = transcribe_audio(audio_path)

    # Summarize transcription
    summary = summarize_text(transcription)

    # Delete temp audio file
    os.remove(audio_path)

    return transcription, summary



with gr.Blocks() as app:
    gr.Markdown("# Video Analyzer: Upload or Download from YouTube")
    
    with gr.Tab("Analyze"):
        upload_video_input = gr.File(label="Upload Video File")
        analyze_btn1 = gr.Button("Analyze Video")
        #analysis_output1 = gr.Textbox(label="Analysis Result")
        outputs=[
            gr.Textbox(label="Transcript"),
            gr.Textbox(label="Summary")
        ]
        analyze_btn1.click(process_video, inputs=upload_video_input, outputs=outputs)
    
    with gr.Tab("Download & Analyze"):
        url_input = gr.Textbox(label="YouTube URL")
        download_btn = gr.Button("Download Video")
        downloaded_video_output = gr.Textbox(label="Downloaded Video Path")
        analyze_btn2 = gr.Button("Analyze Downloaded Video")
        outputs2=[
            gr.Textbox(label="Transcript"),
            gr.Textbox(label="Summary")
        ]
        #analysis_output2 = gr.Textbox(label="Analysis Result")
        
        download_btn.click(download_video, inputs=url_input, outputs=downloaded_video_output)
        analyze_btn2.click(process_video, inputs=downloaded_video_output, outputs=outputs2)


# Check if a GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Launch the Gradio app
#app.launch(share=True) # To make it publicly accessible
#app.launch(server_name="0.0.0.0", server_port=7860) # default port
app.launch(server_name="0.0.0.0", server_port=7880)