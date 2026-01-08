from pathlib import Path


def ask_video_path() -> Path:
    while True:
        path = input("Введите путь к видеофайлу:\n> ").strip('" ').strip()
        video = Path(path)

        if video.exists() and video.is_file():
            return video

        print("❌ Файл не найден. Попробуйте ещё раз.\n")