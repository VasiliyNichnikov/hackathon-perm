from flask import Blueprint, render_template, abort
from app.core.garbage_search import GarbageSearch
from app.core.fileutils import is_video, is_image

module = Blueprint("analytics", __name__)


@module.route("/display/<filename>")
def analytics_show_media(filename: str) -> str:
    garage_search = GarbageSearch(filename)
    garage_search.calculate()
    if is_image(filename):
        return render_template("analytics.html", image_file="upload/" + filename)
    elif is_video(filename):
        return render_template("analytics.html", video_file="upload/" + filename)
    abort(400)
