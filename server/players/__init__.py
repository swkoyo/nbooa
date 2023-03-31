from flask import Blueprint

bp = Blueprint("players", __name__)

from main import routes
