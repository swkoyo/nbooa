from config import URL_PREFIX
from flask import Blueprint
from services import player_service

player_route = Blueprint("player_route", __name__, url_prefix=f"/{URL_PREFIX}/players")


@player_route.route("/", methods=["GET"])
def get_players():
    return player_service.find_players()
