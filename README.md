# SilenceRemover 🎥🔊

SilenceRemover is a Python script that enables you to remove silent parts from a video, automatically. It is especially useful for editing long videos, interviews, or any type of content where you want to eliminate unnecessary silences to make the video more engaging.

## Features 🚀

- **Automatic Silence Detection**: It analyzes the audio track of your video and calculates the loudness of each segment to determine which parts are silent.
- **Configurable Thresholds**: You can easily modify the threshold ratio to determine what is considered silence.
- **GPU Acceleration for Video Encoding** (optional): Uses NVIDIA NVENC for faster video encoding.
- **FFmpeg Dependency Resolution**: If FFmpeg is not found in your system, the script will automatically download and extract it for you.
- **GUI File Picker**: A simple GUI dialog that lets you choose the input video file effortlessly.

## How it Works 🤔

1. SilenceRemover first divides the audio track into small chunks and calculates the loudness of each chunk.
2. It then calculates an average loudness and establishes a threshold. Anything below this threshold is considered silence.
3. The video is then split into segments where the audio is above the threshold.
4. These segments are concatenated into a new video which is free of the silent parts.

## Quick Start 🚀

1. Make sure you have Python installed on your system.
2. Clone this repository or download the script.
3. Execute the script. It will automatically open a file dialog to choose a video.
4. Choose your video and wait for the process to finish.
5. Find the output video named `output.mp4` in the same directory as the script.

## Configuration 🛠

There are a few parameters you can tweak inside the script to better suit your needs:

- `chunk_size` - Length of audio chunks for loudness analysis in milliseconds (default is 250ms).
- `threshold_ratio` - The ratio of the average loudness to consider as the threshold for silence (default is 0.6).
- `margin_size` - Length of margin in milliseconds to be added at the end of clips (default is 250ms).

## Requirements ✅

- Python 3.x
- MoviePy
- NumPy
- Requests
- Tkinter

**## TODO List for Future Enhancements 📝💡

- **Custom Output File Name and Location**: Allow users to choose the output file name and location through the GUI, instead of defaulting to `output.mp4` in the script's directory.

- **User Interface**: Develop a graphical user interface (GUI) to make it easier for non-technical users to operate the script without modifying code.

- **Threshold Customization through GUI**: Allow users to set the threshold for silence detection through the GUI, instead of editing the script.

- **Batch Processing**: Implement a feature that allows users to process multiple video files at once, rather than one at a time.

- **Audio Visualization**: Include an audio waveform visualization in the GUI, so users can visually inspect where silences are detected.

- **Logging and Error Handling**: Implement logging and robust error handling to facilitate troubleshooting and ensure a smooth user experience.

- **Adjustable Margin Sizes**: Allow users to configure the margin size at the beginning and end of each clip separately.

- **Preview Before Export**: Provide an option to preview the edited video before saving the final output.

- **Export to Different Formats**: Allow users to choose from different video formats for the output file.

- **Adjustable Video and Audio Quality**: Implement settings for output video and audio quality/compression.

## Note 📝

This script uses the GPU for encoding the video, which requires an NVIDIA GPU. If you do not have an NVIDIA GPU, you will need to modify the script to use a different encoder.

## License 📄

See `LICENSE` for more information.


