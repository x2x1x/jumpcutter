import sys
import os
import shutil
import zipfile
import requests
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
from tkinter import filedialog
from tkinter import Tk


def calculate_loudness(audio_chunk):
    return np.sqrt(np.mean(np.square(audio_chunk.to_soundarray())))


def remove_silence_from_video(input_video, output_video):
    clip = VideoFileClip(input_video)
    audio = clip.audio

    chunk_size = 250  # ms
    threshold_ratio = 0.6
    margin_size = 250  # ms, margin between clips

    chunks = [audio.subclip(t, t + chunk_size / 1000)
              for t in np.arange(0, audio.duration, chunk_size / 1000)]

    average_loudness = np.mean([calculate_loudness(chunk) for chunk in chunks])

    threshold = average_loudness * threshold_ratio

    valid_clips = []
    start_time = 0
    end_time = 0
    for i, chunk in enumerate(chunks):
        loudness = calculate_loudness(chunk)
        if loudness >= threshold:
            end_time = (i + 1) * chunk_size / 1000
        else:
            if start_time < end_time:
                # Add an additional margin to the end_time
                margin_end_time = min(end_time + margin_size / 1000, audio.duration)
                valid_clips.append(clip.subclip(start_time, margin_end_time))
            start_time = (i + 1) * chunk_size / 1000

    final_clip = concatenate_videoclips(valid_clips)

    # Use GPU with CUDA for encoding the video
    # -c:v h264_nvenc uses the NVENC encoder
    final_clip.write_videofile(output_video, audio_codec="aac", threads=24,
                               ffmpeg_params=['-c:v', 'h264_nvenc'])

    final_clip.close()
    clip.close()
    audio.close()


    final_clip = concatenate_videoclips(valid_clips)

    # Use GPU with CUDA for encoding the video
    # -c:v h264_nvenc uses the NVENC encoder
    final_clip.write_videofile(output_video, audio_codec="aac", threads=24,
                               ffmpeg_params=['-c:v', 'h264_nvenc'])

    final_clip.close()
    clip.close()
    audio.close()

def download_ffmpeg():
    download_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"

    response = requests.get(download_url, stream=True)
    with open("ffmpeg.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    extraction_path = "ffmpeg"
    with zipfile.ZipFile("ffmpeg.zip", 'r') as zip_ref:
        zip_ref.extractall(extraction_path)

    for root, dirs, files in os.walk(extraction_path):
        if 'ffmpeg.exe' in files:
            shutil.copy(os.path.join(root, 'ffmpeg.exe'), ".")
            print("FFmpeg binaries downloaded and extracted.")
            return

    print("Failed to find ffmpeg.exe in the extracted files.")


# Check if FFmpeg is installed
try:
    import imageio_ffmpeg as ffmpeg
except ImportError:
    print("FFmpeg not found, downloading...")
    download_ffmpeg()

# Open file dialog for selecting video file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])

# Process the selected video file
if file_path:
    output_video = "output.mp4"
    remove_silence_from_video(file_path, output_video)
else:
    print("No file selected.")
