from pathlib import Path


def ask_root_folder() -> Path:
    while True:
        path = input("Введите путь к папке с видео:\n> ").strip('" ').strip()
        folder = Path(path)

        if folder.exists() and folder.is_dir():
            return folder

        print("❌ Папка не найдена. Попробуйте ещё раз.\n")