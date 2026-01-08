def ask_screens_count(default: int = 5) -> int:
    raw = input(f"Сколько скринов делать для каждого видео? (по умолчанию {default}):\n> ").strip()
    return int(raw) if raw.isdigit() and int(raw) > 0 else default