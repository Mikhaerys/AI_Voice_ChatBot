import os
import time
import shutil
import audio_manager
import llama_responder
import chatgpt_responder
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def scan_files(folder_path, scanned_files):
    files = os.listdir(folder_path)
    for file in files:
        if file != "README.md":
            file_path = os.path.join(folder_path, file)
            if file_path not in scanned_files:
                scanned_files.append(file_path)
    return scanned_files


def move_file(file_path, folder_path="Processed"):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        shutil.move(file_path, folder_path)
    except Exception as e:
        print(f"Error moving file: {e}")


def main():
    scanned_files = []
    audio_controller = audio_manager.AudioManager()

    USE_CHATGPT = False  # Set to True to use ChatGPT, False to use Llama
    if USE_CHATGPT:
        api_key = os.getenv("OPENAI_API_KEY")
        ai_responder = chatgpt_responder.ChatGPTResponder(api_key)
    else:
        ai_responder = llama_responder.LlamaResponder()

    while True:
        start_time = time.time()
        scanned_files = scan_files("Inputs", scanned_files)
        if not scanned_files:
            print("No new files found. Waiting for 1 second...")
            end_time = time.time()
            time.sleep(1)
            continue
        try:
            prompt = audio_controller.audio2text(scanned_files[0])
        except Exception as e:
            print(f"Error converting audio to text: {e}")
            end_time = time.time()
            time.sleep(1)
            continue

        response = ai_responder.get_response(prompt)
        audio_controller.text2audio(response)

        move_file(scanned_files[0])
        scanned_files.pop(0)

        end_time = time.time()
        print(f"Response time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
