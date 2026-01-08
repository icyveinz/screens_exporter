from pathlib import Path
from constants import VIDEO_EXTENSIONS


def find_video_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS
    ]