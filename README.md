# 🎬 Video Analyzer

A Python application that downloads YouTube videos, transcribes them using OpenAI Whisper, and generates AI-powered summaries using Ollama.


![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-GPU_Enabled-red?logo=pytorch&logoColor=white)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?logo=openai&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-Interface-orange?logo=gradio&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black?logo=ollama&logoColor=white)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Audio-green?logo=ffmpeg&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-GPL--3.0-blue)


## 🚀 Features

- 📥 Download videos from YouTube
- 📤 Upload local video files
- 🎤 Automatic speech-to-text transcription using Whisper
- 📝 AI-powered summarization using Ollama
- 🌐 Web interface powered by Gradio
- 🚀 GPU acceleration support

## 📋 Prerequisites

- Python 3.12.3+
- CUDA-compatible GPU
- Ollama servide (running local or remotely) (default model: llama3.3)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bigdatawirtz/vsummarizer.git
cd vsummarizer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
OLLAMA_HOST=localhost
```

## Usage

1. Start the application:
```bash
python main_gui.py
```

2. Access the web interface at `http://localhost:7880` (or from any device on your network at `http://YOUR_IP:7880`)

3. Choose one of two options:
   - **Analyze Tab**: Upload a video file directly
   - **Download & Analyze Tab**: Paste a YouTube URL to download and analyze

4. Click the analyze button and wait for the transcription and summary

## Requirements

Install `requirements.txt` file with:

```
pip install -r requirements.txt
```

## Project Structure

```
vsummarizer/
├── main_gui.py           # Main application file
├── .env                  # Environment configuration
├── requirements.txt      # Python dependencies
├── downloads/            # Downloaded videos (auto-created)
└── data/                 # Temporary audio files (auto-created)
```

## How It Works

1. **Video Input**: Accept video via upload or YouTube download
2. **Audio Extraction**: Extract audio track using ffmpeg
3. **Transcription**: Convert speech to text using Whisper AI
4. **Summarization**: Generate concise summary using Ollama
5. **Cleanup**: Remove temporary files

## GPU Support

The application automatically detects and uses CUDA-enabled GPUs for faster Whisper transcription. If no GPU is available, it falls back to CPU processing.


## Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) for speech recognition
- [Ollama](https://ollama.ai/) for AI summarization
- [Gradio](https://gradio.app/) for the web interface
- [pytubefix](https://github.com/JuanBindez/pytubefix) for YouTube downloads