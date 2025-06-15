from pydub import AudioSegment
import os

os.environ["PATH"] += os.pathsep + r"C:\Users\sweth\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"

AudioSegment.ffmpeg = r"C:\Users\sweth\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\sweth\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin\ffprobe.exe"

sound = AudioSegment.from_mp3("audio.mp3")
sound.export("move_sound.wav", format="wav")
sound = AudioSegment.from_mp3("audio1.mp3")
sound.export("capture_sound.wav", format="wav")
print("✅ MP3 to WAV conversion successful!")
