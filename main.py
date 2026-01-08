from functions.ask_screens_count import ask_screens_count
from functions.ask_video_path import ask_video_path
from functions.make_screenshots import make_screenshots

def main():
    print("🎬 Скрипт для создания скринов из видео\n")

    video_path = ask_video_path()
    count = ask_screens_count()

    make_screenshots(video_path, count)


if __name__ == "__main__":
    main()