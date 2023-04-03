from datetime import datetime

from flask import jsonify
from models.player import Player
from schemas.player import PlayerSchema
from utils import date, scrapper

player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


def find_players():
    players = Player.query.all()
    return jsonify(players_schema.dump(players))


def find_player_stats(_id):
    player = Player.query.filter_by(_id=_id).first()
    if player:
        latest_season = player.end_year if player.end_year else date.get_current_year()
        game_log = scrapper.get_game_logs(player._id, latest_season)
        bday_log = game_log[
            game_log.Date.str.contains(date.generate_date_regex(player.birthday))
        ]
        xmas_log = game_log[
            game_log.Date.str.contains(
                date.generate_date_regex(date.get_christmas_date())
            )
        ]
        ny_log = game_log[
            game_log.Date.str.contains(
                date.generate_date_regex(date.get_new_years_date())
            )
        ]
        vale_log = game_log[
            game_log.Date.str.contains(
                date.generate_date_regex(date.get_valentines_date())
            )
        ]
        game_logs = {
            "birthday": bday_log.to_dict(orient="records")[0]
            if not bday_log.empty
            else None,
            "christmas": xmas_log.to_dict(orient="records")[0]
            if not xmas_log.empty
            else None,
            "new_years": ny_log.to_dict(orient="records")[0]
            if not ny_log.empty
            else None,
            "valentines": vale_log.to_dict(orient="records")[0]
            if not vale_log.empty
            else None,
        }
        data = player_schema.dump(player)
        data["game_logs"] = game_logs
        return jsonify(data)
    else:
        return {"message": "Player not found"}, 404
