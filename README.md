# AI_Voice_ChatBot

## Project Description
**AI_Voice_ChatBot** is a Python-based project that allows users to ask questions via audio, converts the audio input to text, sends the text to an AI model (either ChatGPT or Llama), and converts the AI's response back into audio. The project supports seamless interaction through voice queries and audio responses, using different AI models depending on user preference.


## Features

- Audio input processing for user questions
- Support for multiple AI models (ChatGPT and Llama)
- Text-to-speech conversion for AI responses
- Automatic file management for processed audio files
- Real-time monitoring of input directory
- Response time tracking

## Project Structure

```
AI_Voice_ChatBot/
├── Inputs/              # Directory for user audio question files
├── Processed/          # Directory for processed audio files
├── audio_manager.py    # Handles audio conversion and processing
├── chatgpt_responder.py # ChatGPT API integration
├── llama_responder.py   # Llama model integration
├── main.py             # Main application logic
├── requirements.txt    # Project dependencies
└── .gitignore         # Git ignore configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mikhaerys/AI_Voice_ChatBot.git
cd AI_Voice_ChatBot
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Install the command-line tool [`ffmpeg`](https://ffmpeg.org/) from the official page or with the next command:
```bash
# on Windows
winget install ffmpeg
```

5. Configure your AI model:
    - For ChatGPT: Save your API key in a local `.env` file with the following content:
    ```env
    CHATGPT_API_KEY=your_api_key_here
    ```
    - For Llama: Ensure that Llama 3.2 and the `ollama` library are properly downloaded and configured. You can find the necessary files and instructions on [Ollama's website](https://ollama.com).

## Usage

1. Place audio files containing your questions in the `Inputs` directory.

2. Run the application:
```bash
python main.py
```
3. Note: The initial run may take some time as the Whisper model needs to be downloaded.

4. The system will:
    - Monitor the `Inputs` directory for new audio files
    - Convert audio to text
    - Process the question using the selected AI model
    - Generate an audio response
    - Save the audio response as `output.mp3`
    - Move processed files to the `Processed` directory

## Configuration

To switch between AI models, modify the `USE_CHATGPT` flag in `main.py`:
```python
USE_CHATGPT = True  # Use ChatGPT
# or
USE_CHATGPT = False # Use Llama
```

## How It Works

1. **Input Processing**:
    - The system continuously monitors the `Inputs` directory for new audio files
    - When a new file is detected, it's converted to text using the `audio_manager.py` module

2. **AI Processing**:
    - The text is sent to either ChatGPT or Llama (based on configuration)
    - The AI model generates a response

3. **Output Generation**:
    - The AI's text response is converted back to audio
    - The original input file is moved to the `Processed` directory

4. **Performance Monitoring**:
    - Response times are logged for each interaction

## Requirements

- Python 3.x
- Internet connection (for ChatGPT API)
- ollama library and Llama 3.2
- The command-line tool [`ffmpeg`](https://ffmpeg.org/) (Whisper requirement)
- Required Python packages (specified in requirements.txt)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.