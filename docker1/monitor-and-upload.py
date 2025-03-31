import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

UPLOAD_URL = "http://your-server.com/upload"  # Replace with your endpoint
WATCH_FOLDER = "/watch_folder"  # Must be mounted in Docker

class ImageUploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f"New image detected: {event.src_path}")
            self.upload_image(event.src_path)

    def upload_image(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                files = {'file': (os.path.basename(file_path), f)}
                response = requests.post(UPLOAD_URL, files=files)
                if response.status_code == 200:
                    print(f"Successfully uploaded: {file_path}")
                else:
                    print(f"Upload failed: {response.text}")
        except Exception as e:
            print(f"Error uploading {file_path}: {e}")

if __name__ == "__main__":
    event_handler = ImageUploadHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"Monitoring folder: {WATCH_FOLDER}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()