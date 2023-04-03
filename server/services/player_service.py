from flask import jsonify
from models.player import Player
from schemas.player import PlayerSchema

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


def find_players():
    players = Player.query.all()
    return jsonify(players_schema.dump(players))
