from models.player import Player
from schemas.client import ma


class PlayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Player
