import os
from pathlib import Path

from dotenv import load_dotenv


def get_project_root():
    return Path(__file__).parent.parent


def get_env_path():
    return os.path.join(get_project_root(), ".env")


def load_env():
    load_dotenv(get_env_path())


load_env()


def get_secret_key() -> str:
    return os.environ.get("SECRET_KEY")


def get_upload_folder() -> str:
    root = get_project_root()
    folder = os.path.join(root, "static/upload")
    if not os.path.exists(folder):
        os.makedirs(folder)
    return os.path.join(root, "static/upload")
