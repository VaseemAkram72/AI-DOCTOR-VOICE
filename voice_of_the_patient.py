# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup Audio recorder (ffmpeg & portaudio)
# ffmpeg, portaudio, pyaudio
# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step1: Setup Audio recorder (ffmpeg & portaudio)
# ffmpeg, portaudio, pyaudio

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def record_audio(file_path, timeout=20, phrase_time_limit=None):

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            logging.info("Adjusting for ambient noise...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            logging.info("Start speaking now...")

            audio_data = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

            logging.info("Recording complete.")

            wav_data = audio_data.get_wav_data()

            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))

            audio_segment.export(
                file_path,
                format="mp3",
                bitrate="128k"
            )

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:

        logging.error(f"An error occurred: {e}")


audio_filepath = "patient_voice_test_for_patient.mp3"

# record_audio(file_path=audio_filepath)


# ==========================================================
# Step2: LOCAL WHISPER SPEECH TO TEXT
# ==========================================================

import whisper

# Load Whisper Model
model = whisper.load_model("base")


def transcribe_with_groq(
    stt_model,
    audio_filepath,
    GROQ_API_KEY
):

    try:

        if audio_filepath is None:
            return "No audio file detected"

        result = model.transcribe(audio_filepath)

        transcription_text = result["text"]

        return transcription_text

    except Exception as e:

        return f"Transcription Error: {str(e)}"