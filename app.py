from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_classful import FlaskView, route


app = Flask(__name__)


@app.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")


class Dashboard(FlaskView):
    @route('/dashboard', methods=["GET"])
    def watchlist(self):
        return render_template("test.html")


class Watchlist(FlaskView):
    @route('/watchlist', methods=["GET", "POST"])
    def watchlist(self):
        if request.method == "GET":
            return render_template("input_box_watchlist.html")
        else:
            num = request.form["num"]
            return redirect(url_for("Watchlist:watchlist_num", num=num))

    @route('/watchlist/<int:num>')
    def watchlist_num(self, num):
        return f"Num = {num}"


Watchlist.register(app, route_base="/")
Dashboard.register(app, route_base="/")

if __name__ == "__main__":
    app.run(debug=True)