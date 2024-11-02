from moviepy.editor import VideoFileClip
from video_downloader import download_from_yandex_disk
from vosk import Model, KaldiRecognizer, SetLogLevel
from transformers import pipeline
from pydub import AudioSegment
import json
import os


def transcribe_audio_from_video(video_url, model_path, video_path='video.mp4', audio_path='audio.wav'):
    # Скачиваем видео
    download_from_yandex_disk(video_url, video_path)
    
    # Извлекаем аудио из видео
    def extract_audio(video_path, audio_path):
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    
    extract_audio(video_path, audio_path)
    
    # Настройки модели и распознавания
    SetLogLevel(0)
    FRAME_RATE = 16000
    CHANNELS = 1

    if not os.path.exists(model_path):
        print("Please download the model from https://alphacephei.com/vosk/models and unpack it.")
        return None

    model = Model(model_path)
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    # Предобработка аудио и извлечение текста
    audio = AudioSegment.from_file(audio_path).set_channels(CHANNELS).set_frame_rate(FRAME_RATE)
    rec.AcceptWaveform(audio.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]

    return text

def retelling(text):
    # Загрузка модели для суммаризации
    summarizer = pipeline("summarization", model="IlyaGusev/rubert-base-cased-summarization")
    
    # Генерация пересказа
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']




# Использование функции
video_url = 'https://disk.yandex.ru/i/271ogJDCZFYZNw'
model_path = "models/vosk-model-small-ru-0.22"
text = transcribe_audio_from_video(video_url, model_path)
print("Извлечённый текст:", text)
text_summary = retelling(text)
print("Пересказанный текст:", text_summary)
