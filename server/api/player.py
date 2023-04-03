from flask import Blueprint, request

player_route = Blueprint("player_route", __name__)


@player_route.route("/players", methods=["GET"])
def get_players():
    return "hi"
