import subprocess
from pathlib import Path


def ask_video_path() -> Path:
    while True:
        path = input("Введите путь к видеофайлу:\n> ").strip('" ').strip()
        video = Path(path)

        if video.exists() and video.is_file():
            return video

        print("❌ Файл не найден. Попробуйте ещё раз.\n")


def ask_screens_count(default: int = 5) -> int:
    raw = input(f"Сколько скринов сделать? (по умолчанию {default}):\n> ").strip()
    return int(raw) if raw.isdigit() and int(raw) > 0 else default


def get_video_duration(video_path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    return float(result.stdout.strip())


def make_screenshots(video_path: Path, count: int):
    screens_dir = video_path.parent / "screens"
    screens_dir.mkdir(exist_ok=True)

    duration = get_video_duration(video_path)

    timestamps = [
        duration * (i + 1) / (count + 1)
        for i in range(count)
    ]

    saved = 0

    for idx, ts in enumerate(timestamps, start=1):
        output_file = screens_dir / f"screen_{idx:02d}.jpg"

        subprocess.run(
            [
                "ffmpeg",
                "-ss", str(ts),
                "-i", str(video_path),
                "-frames:v", "1",
                "-q:v", "2",
                str(output_file),
                "-y",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )

        if output_file.exists():
            saved += 1
            print(f"✔ Сохранён: {output_file.name}")
        else:
            print(f"❌ Не удалось сохранить: {output_file.name}")

    print(f"\n✅ Сохранено {saved}/{count} скринов в:\n{screens_dir}")


def main():
    print("🎬 Скрипт для создания скринов из видео\n")

    video_path = ask_video_path()
    count = ask_screens_count()

    make_screenshots(video_path, count)


if __name__ == "__main__":
    main()
