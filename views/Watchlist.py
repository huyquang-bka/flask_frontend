from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)


@app.route("/watchlist", methods=["GET"])
def watchlist(self):
    return "This is WatchList"