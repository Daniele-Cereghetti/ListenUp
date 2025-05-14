# ListenUp 
Listen-Up is a web application built with Python and Flask that enables automatic transcription of .opus audio files, commonly used by WhatsApp. The app leverages OpenAI's Whisper speech recognition model to accurately convert voice messages into text. Designed for accessibility and ease of use, Listen-Up features a simple interface for uploading audio files, initiating transcription, and viewing results directly in the browser. There is no need to specify the language of the audio — Whisper automatically detects it.

## Installation
1. Choose a Whisper Model Image<br>
   Whisper is available in multiple sizes: tiny, base, small, medium, and large.
   More info about openai's models click [here](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages).<br>
   If you change the model, you have to change in app.py and in the Dockerfile, it must match. <br><br>
   💡 By default, small is used — it's fast, accurate in most cases, and rarely makes mistakes. Even when it does, the context usually makes the meaning clear. It occpuies ~2GB of RAM

2. Build Docker image<br>
   Enter in the root project and run:
   ```
   docker build -t listen-up .
   ```
3. Run Docker container<br>
   One you build the image you can run it with:
   ```
   docker run -d --name listen-up -p 5000:5000 listen-up
   ```
