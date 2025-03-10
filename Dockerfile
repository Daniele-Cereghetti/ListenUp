FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install --no-cache-dir torch==2.2.0+cpu torchvision==0.17.0+cpu torchaudio==2.2.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "import whisper; whisper.load_model('small')"

EXPOSE 5000

CMD ["python", "server.py"]