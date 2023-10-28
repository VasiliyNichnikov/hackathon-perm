from app.core.pathutils import get_upload_folder, get_secret_key
import app.core.fileutils as file_utils


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = get_secret_key()
    UPLOAD_FOLDER = get_upload_folder()
    UPLOAD_EXTENSIONS = file_utils.UPLOAD_EXTENSIONS
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
