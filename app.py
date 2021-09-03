from flask import Flask
from flask_graphql import GraphQLView

from commands import create_tables
from config import Config
from extensions import db


from api.schema import schema

def register_extensions(app):
    db.init_app(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.cli.add_command(create_tables)

    register_extensions(app)

    app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphq',
        schema=schema,
        graphiql=False
    )
)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
