from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap4
import csv
from cafe_form import MyForm

app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.secret_key = "fsjdl2342ljf@#$%"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def display_cafes():
    cafe_data = []
    with open("cafe-data.csv", mode="r", newline='') as fd:
        data = csv.DictReader(fd)
        for row_data in data:
            cafe_data.append(row_data)
    return render_template("cafes.html", data=cafe_data)


@app.route('/add', methods=["GET", "POST"])
def add_row():
    form = MyForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", newline='') as file:
            file.write(f"\n{form.cafe_name.data},"
                       f"{form.location.data},"
                       f"{form.open_time.data},"
                       f"{form.close_time.data},"
                       f"{form.quality_select.data},"
                       f"{form.strength_select.data},"
                       f"{form.power_select.data}")
        return redirect(url_for('display_cafes'))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
