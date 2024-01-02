import os

import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase

__version__ = (1, 1, 0, "dev")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # some deploy systems set the database url in the environment
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

    from magic_ledger import projects

    app.register_blueprint(projects.bp)

    from magic_ledger import third_prties

    app.register_blueprint(third_prties.bp)

    from magic_ledger import inventory

    app.register_blueprint(inventory.bp)

    from magic_ledger import invoices

    app.register_blueprint(invoices.bp)

    from magic_ledger import account_plan

    app.register_blueprint(account_plan.bp)

    from magic_ledger import transactions

    app.register_blueprint(transactions.bp)

    from magic_ledger import assets

    app.register_blueprint(assets.bp)

    from magic_ledger import financial_holdings

    app.register_blueprint(financial_holdings.bp)

    from magic_ledger import liquidity

    app.register_blueprint(liquidity.bp)

    return app


def init_db():
    db.drop_all()
    db.configure_mappers()
    db.create_all()
    db.session.commit()


# add a python function that inserts all the entries in the accounts.sql file into the database
def insert_account_plan():
    with open(
        r"C:\Users\ageor\PycharmProjects\magic-ledger\magic_ledger\accounts.sql",
        mode="r",
    ) as sql_file:
        for line in sql_file:
            db.session.execute(text(line))
            db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
    insert_account_plan()
    click.echo("provisionsed account plan.")
