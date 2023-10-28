from flask import Blueprint, render_template, abort
from app.core.controller_by_data_output import ControllerByDataOutput
from app.core.fileutils import is_video, is_image

module = Blueprint("analytics", __name__)


@module.route("/display/<filename>")
def analytics_show_media(filename: str) -> str:
    output = ControllerByDataOutput()
    view_data = output.get_view_data(filename)

    if is_image(filename):
        return render_template("analytics2.html", image_file=view_data.box_path, image_chart_file=view_data.chart_path, messages=view_data.messages)
    elif is_video(filename):
        return render_template("analytics.html", video_file="upload/box/" + filename)
    abort(400)
