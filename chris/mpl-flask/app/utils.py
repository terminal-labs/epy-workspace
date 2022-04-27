ALLOWED_EXTENSIONS = {"txt", "csv"}


def allowed_file(filename):
    """Verify that uploaded file is of the appropriate type/extension"""

    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def transform_csv_data(data):
    """Convert CSV data into appropriate types for objects passed to matplotlib"""

    labels = data.pop(0)
    xlabel, ylabel = labels[0], labels[1]
    x = [int(obj[0]) for obj in data]
    y = [float(obj[0]) for obj in data]

    return dict(
        xlabel=xlabel,
        ylabel=ylabel,
        x=x,
        y=y,
    )


def ts_for_filename():
    """Timestamp of current time for unique file names: '20211019162019.313346'"""

    now = datetime.datetime.now()
    ts = now.strftime("%Y%m%d%H%M%S.%f")

    return ts
