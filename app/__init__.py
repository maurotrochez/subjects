import os
from dotenv import Dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dotenv_path = Dotenv(os.path.join(os.getcwd(), ".env"))
os.environ.update(dotenv_path)

db_setup = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
    os.environ.get('USERNAME'),
    os.environ.get('PASSWORD'),
    os.environ.get('HOST'),
    os.environ.get('PORT'),
    os.environ.get('DATABASE'),
)

engine = create_engine(db_setup)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def create_app(app):
    Base.metadata.create_all(engine)

    from .api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
