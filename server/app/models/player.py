from app.extensions import db
from sqlalchemy.sql import func


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    def __repr__(self):
        return f'<Player "{self.first_name} {self.last_name}">'
