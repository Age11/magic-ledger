import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

__version__ = (1, 1, 0, "dev")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # some deploy systems set the database url in the environ
    db_url = os.environ.get("DATABASE_URL")

    if db_url is None:
        # default to a sqlite database in the instance folder
        db_url = "sqlite:///db.sqlite"

    app.config.from_mapping(
        # default secret that should be overridden in environ or config
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        SQLALCHEMY_DATABASE_URI=db_url,
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # initialize Flask-SQLAlchemy and the init-db command
    db.init_app(app)
    app.cli.add_command(init_db_command)

    # apply the blueprints to the app
    from magic_ledger import organizations
    app.register_blueprint(organizations.bp)

    from magic_ledger import address_book
    app.register_blueprint(address_book.bp)

    from magic_ledger import inventory
    app.register_blueprint(inventory.bp)

    from magic_ledger import invoices
    app.register_blueprint(invoices.bp)

    from magic_ledger import inventory_item
    app.register_blueprint(inventory_item.bp)

    # app.register_blueprint(blog.bp)

    return app


def init_db():
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
