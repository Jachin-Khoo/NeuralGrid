# agent_uploader.py
import os
import time
from config import client, Types

def upload_file_to_gemini(file_path, mime_type=None):
    """Uploads a file to Gemini and waits for it to be processed (best effort)."""
    print(f" >> Uploading {file_path} to Gemini...")
    try:
        if mime_type:
            upload_config = Types.UploadFileConfig(
                display_name=os.path.basename(file_path),
                mime_type=mime_type,
            )
            file_ref = client.files.upload(
                file=file_path,
                config=upload_config,
            )
        else:
            file_ref = client.files.upload(file=file_path)

        state = getattr(file_ref, "state", None)
        while state and getattr(state, "name", None) == "PROCESSING":
            print(".", end="", flush=True)
            time.sleep(1)
            file_ref = client.files.get(name=file_ref.name)
            state = getattr(file_ref, "state", None)

        if state and getattr(state, "name", None) == "FAILED":
            raise ValueError(f"File {file_path} failed to process on Gemini side.")

        print(f"\n >> File ready: {getattr(file_ref, 'display_name', file_path)}")
        return file_ref
    except Exception as e:
        print(f"\nError uploading file: {e}")
        return None
