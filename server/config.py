import os

import dotenv

dotenv.load_dotenv()

VERSION = int(os.environ.get("VERSION"))
URL_PREFIX = f"/v{VERSION}"
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'db', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
