"""Main blueprint"""

import csv

from flask import (
    Blueprint,
    current_app,
    redirect,
    render_template,
)
from matplotlib import pyplot as plt

from app.forms import DataForm
from app.utils import transform_csv_data, ts_for_filename

bp = Blueprint("main", __name__)


@bp.route("/", methods=("GET", "POST"))
def home():
    form = DataForm()
    if form.validate_on_submit():

        # Process data
        with open(form.upload.data, "r") as buffer:
            reader = csv.reader(buffer)
            data = [row for row in reader]
            transformed = transform_csv_data(data)

        # Set up plot
        plt.bar(transformed["x"], transformed["y"])
        plt.title("Values by day")
        plt.xlabel(transformed["xlabel"])
        plt.ylabel(transformed["ylabel"])

        # Save plot image
        filename = f"{ts_for_filename()}-plot.png"
        dir_ = current_app.config["UPLOAD_DIR"]  # Returns Posix object
        target = str(dir_ / filename)
        plt.savefig(target)

        # `pyplot` objects can cause memory leaks - explicitly close...
        plt.close()

        # Redirect to canvas display
        return redirect("main.show", figure=figure)

    return render_template("main/index.html", form=form)


@bp.route("/show/<figure>")
def show_with_figure(figure):
    return render_template("main/show.html", figure=filename)
