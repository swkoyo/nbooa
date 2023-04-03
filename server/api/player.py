from config import URL_PREFIX
from flask import Blueprint, request
from services import player_service

player_route = Blueprint("player_route", __name__, url_prefix=f"/{URL_PREFIX}/players")


@player_route.route("/", methods=["GET"])
def get_players():
    return player_service.find_players()


@player_route.route("/<string:_id>", methods=["GET"])
def get_player_stats(_id):
    return player_service.find_player_stats(_id)
