# pip install -U openai-whisper
# instale também o ffmpeg

import whisper

# Carrega o modelo que você quer
model = whisper.load_model("medium")

# Caminho para o seu arquivo de áudio
audio_path = "exemplo_audio.mp3"  # pode ser .wav, .mp3, .m4a, etc.

# Transcreve o áudio
result = model.transcribe(audio_path)

# Exibe a transcrição no console
print(result["text"])

# Salva a transcrição em um arquivo de texto
with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
