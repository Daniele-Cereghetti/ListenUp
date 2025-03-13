from flask import Flask, request, render_template
import whisper, tempfile, ffmpeg

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024  # 30 MB limit

model = whisper.load_model("small", device="cpu")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'Errore: Nessun file inviato', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Errore: Nome file vuoto', 400
    
    try:
        file_data = file.read()
        file_size = len(file_data)

        if file_size == 0:
            return 'Errore: File vuoto', 400
        
        with tempfile.NamedTemporaryFile(delete=True, suffix=".opus") as audio_opus:
            audio_opus.write(file_data)
            audio_opus.flush()

            with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as audio_mp:
                ffmpeg.input(audio_opus.name).output(audio_mp.name, audio_bitrate="192k").run(overwrite_output=True, quiet=True)
                result = model.transcribe(audio_mp.name)
        
        return f'Trascrizione: {result["text"]}'
    
    except Exception as e:
        return f'Errore durante la lettura del file: {str(e)}', 500
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
