import subprocess
from pathlib import Path

from functions.get_video_duration import get_video_duration


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