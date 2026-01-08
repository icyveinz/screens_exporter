from functions.ask_root_folder import ask_root_folder
from functions.ask_screens_count import ask_screens_count
from functions.extract_screenshots import extract_screenshots
from functions.find_video_files import find_video_files


def main():
    root_folder = ask_root_folder()
    count = ask_screens_count()

    videos = find_video_files(root_folder)

    if not videos:
        print("❌ В папке не найдено видеофайлов.")
        return

    print(f"\n🔍 Найдено видеофайлов: {len(videos)}\n")

    success = 0
    failed = 0

    for video in videos:
        print(f"▶ Обработка: {video}")

        try:
            saved = extract_screenshots(video, count)
            print(f"  ✔ Скрины сохранены: {saved}/{count}\n")
            success += 1
        except Exception as e:
            print(f"  ❌ Ошибка: {e}\n")
            failed += 1

    print("📊 Итог:")
    print(f"  Успешно обработано: {success}")
    print(f"  С ошибкой: {failed}")


if __name__ == "__main__":
    main()