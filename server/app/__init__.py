from datetime import datetime

from app.extensions import db
from app.models.player import Player
from config import URL_PREFIX, VERSION, Config
from flask import Flask, jsonify
from flask.cli import with_appcontext
from seeders.data import PLAYERS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # from main import bp as main_bp

    # app.register_blueprint(main_bp)

    @app.route(f"/{URL_PREFIX}/health")
    def get_health():
        return {"name": "NBooA API", "status": "OK", "version": VERSION}

    @app.cli.command("seed")
    def seed():
        for player in PLAYERS:
            m, d, y = player["birthday"].split("-")
            new_player = Player(
                first_name=player["first_name"],
                last_name=player["last_name"],
                birthday=datetime(int(y), int(m), int(d)),
                image_url=player["image_url"],
                _id=player["_id"],
                start_year=player["start_year"],
                end_year=player["end_year"],
            )
            db.session.add(new_player)
            db.session.commit()

    return app
