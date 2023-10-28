IMAGES = tuple(".jpg .png".split())
VIDEOS = tuple(".mp4".split())

UPLOAD_EXTENSIONS = IMAGES + VIDEOS


def is_video(file: str) -> bool:
    return is_file_supported(file, VIDEOS)


def is_image(file: str) -> bool:
    return is_file_supported(file, IMAGES)


def is_file_supported(file: str, allowed_extensions: list[str] | tuple[str]) -> bool:
    for allowed_extension in allowed_extensions:
        if file.endswith(allowed_extension):
            return True
    return False
