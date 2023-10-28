from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Создание приложения
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# Подключение файлов
# file_types = IMAGES + tuple("mp4")
# allowed_files = UploadSet("media", file_types)
# configure_uploads(app, allowed_files)


# Подключение blueprints
import app.entity.controllers as entity
import app.analytics.controllers as analytics

app.register_blueprint(entity.module)
app.register_blueprint(analytics.module)
