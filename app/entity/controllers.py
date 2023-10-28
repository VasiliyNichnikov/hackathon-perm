import os.path

from flask import Blueprint, redirect, url_for, render_template, flash, request
from werkzeug.utils import secure_filename

from app import app
from app.core.fileutils import is_file_supported

module = Blueprint("entity", __name__)


@module.route('/')
@module.route('/index')
def index() -> str:
    return render_template("index.html")


# TODO: сейчас не поддерживается русский язык в название файла
@module.route("/upload_video", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return redirect(url_for("entity.index"))

    file = request.files["file"]
    if file.filename == '':
        flash("Файл не выбран")
        return redirect(url_for("entity.index"))
    if not is_file_supported(file.filename, app.config["UPLOAD_EXTENSIONS"]):
        flash("Не верный тип файла")
        return redirect(url_for("entity.index"))
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("analytics.analytics_show_media", filename=filename))

